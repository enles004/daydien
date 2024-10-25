import os

from flask import Flask, render_template, request, redirect, url_for, flash
from werkzeug.utils import secure_filename

from services.draw_tree import draw_mst
from services.prim import prim_alg
from services.random_matrix import generate_random_matrix
from services.read_file import read_input

app = Flask(__name__)
app.secret_key = "supersecretkey"
app.config['UPLOAD_FOLDER'] = './uploads'


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        option = request.form.get('option')
        if option == 'upload':
            if 'file' not in request.files:
                flash('Không có file được chọn.')
                return redirect(request.url)
            file = request.files['file']
            if file.filename == '':
                flash('Không có file được chọn.')
                return redirect(request.url)
            if file:
                filename = secure_filename(file.filename)
                file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
                file.save(file_path)
                try:
                    N, matrix = read_input(file_path)
                except Exception as e:
                    flash(f"Lỗi khi đọc file: {e}")
                    return redirect(request.url)

        elif option == 'random':
            matrix_size = request.form.get('matrix_size')
            if not matrix_size or not matrix_size.isdigit():
                flash('Vui lòng nhập kích thước ma trận hợp lệ.')
                return redirect(request.url)
            N = int(matrix_size)
            if N < 2 or N > 20:
                flash('Kích thước ma trận phải từ 2 đến 20.')
                return redirect(request.url)
            N, matrix = generate_random_matrix(N)

        else:
            flash('Vui lòng chọn một tùy chọn hợp lệ.')
            return redirect(request.url)

        total_length, mst_edges = prim_alg(N, matrix)
        draw_mst(N, mst_edges)
        mst_only = [(u, v) for u, v, w in mst_edges]
        return render_template('result.html',
                               total_length=total_length,
                               mst_edges=mst_edges,
                               matrix=matrix,
                               N=N, mst_only=mst_only)

    return render_template('index.html')


@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return redirect(url_for('static', filename=filename))


if __name__ == '__main__':
    if not os.path.exists(app.config['UPLOAD_FOLDER']):
        os.makedirs(app.config['UPLOAD_FOLDER'])
    if not os.path.exists('./static'):
        os.makedirs('./static')
    app.run(debug=True)
