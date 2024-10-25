def read_input(file_path):
    try:
        with open(file_path, 'r') as file:
            first_line = file.readline().strip()
            if not first_line.isdigit():
                raise ValueError("Dòng đầu tiên phải là một số nguyên dương (số lượng phòng).")
            N = int(first_line)
            if N <= 0:
                raise ValueError("Số lượng phòng phải lớn hơn 0.")

            matrix = []
            for i in range(N):
                line = file.readline()
                if not line:
                    raise ValueError(f"Thiếu dòng dữ liệu cho phòng {i}.")
                row = line.strip().split()
                if len(row) != N:
                    raise ValueError(f"Dòng {i + 2} phải chứa đúng {N} phần tử.")
                try:
                    row_values = list(map(int, row))
                except ValueError:
                    raise ValueError(f"Dòng {i + 2} chứa giá trị không phải số nguyên.")
                if any(x < 0 for x in row_values):
                    raise ValueError(f"Dòng {i + 2} chứa giá trị âm.")
                matrix.append(row_values)

            for i in range(N):
                for j in range(N):
                    if matrix[i][j] != matrix[j][i]:
                        raise ValueError("Ma trận không đối xứng tại vị trí ({}, {}).".format(i, j))

        return N, matrix
    except Exception as e:
        raise e