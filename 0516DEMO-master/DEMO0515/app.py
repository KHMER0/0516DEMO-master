from flask import Flask, jsonify, render_template
import csv
import os

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/category/<category>')
def category(category):
    return render_template('category.html')

@app.route('/api/csv-to-json', methods=['GET'])
def csv_to_json():
    # 指定要读取的CSV文件路径
    csv_file = os.path.join(os.path.dirname(__file__), 'class0515改.csv')
    
    if not os.path.exists(csv_file):
        return jsonify({'error': 'CSV file not found'}), 404
    
    data = []
    with open(csv_file, mode='r', encoding='utf-8') as file:
        csv_reader = csv.DictReader(file)
        for row in csv_reader:
            # 转换每行数据为字典
            data.append(dict(row))
    
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True)