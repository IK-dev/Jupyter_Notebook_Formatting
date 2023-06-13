import nbformat as nbf

# Вказати шлях до файлу .py, який потрібно зчитати
py_file_path = 'python_sourse.py'

# Вказати шлях та ім'я файлу .ipynb, у який зберігатиметься результат
output_path = 'new_jn.ipynb'

# Зчитати вміст файлу .py
with open(py_file_path, 'r', encoding='utf-8') as f:
    py_file_content = f.read()

# Розділити вміст на окремі конструкції (припустимо, що розділювачем є "#%%")
code_blocks = py_file_content.split("\n\n")

# Створити новий Jupyter Notebook
nb = nbf.v4.new_notebook()

# Додати окрему кодову комірку для кожної конструкції
for code_block in code_blocks:
    if code_block.strip():  # Пропустити порожні блоки
        nb['cells'].append(nbf.v4.new_code_cell(code_block))

# Зберегти Jupyter Notebook з розділеними кодовими комірками
nbf.write(nb, output_path)