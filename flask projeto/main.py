from flask import Flask, render_template, request, redirect, url_for
import sqlite3

app = Flask(__name__, static_url_path='/static')

# Função para criar a tabela de itens na base de dados
def create_table():
    conn = sqlite3.connect('marcenaria.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS items
                 (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT, description TEXT, quantity INTEGER)''')
    conn.commit()
    conn.close()

# Rota para exibir todos os itens
@app.route('/')
def show_items():
    conn = sqlite3.connect('marcenaria.db')
    c = conn.cursor()
    c.execute('SELECT * FROM items')
    items = c.fetchall()
    conn.close()
    return render_template('index.html', items=items)

# Rota para adicionar um novo item
@app.route('/add', methods=['POST'])
def add_item():
    name = request.form['name']
    description = request.form['description']
    quantity = request.form['quantity']
    conn = sqlite3.connect('marcenaria.db')
    c = conn.cursor()
    c.execute('INSERT INTO items (name, description, quantity) VALUES (?, ?, ?)', (name, description, quantity))
    conn.commit()
    conn.close()
    return redirect(url_for('show_items'))

# Rota para editar um item existente
@app.route('/edit/<int:item_id>', methods=['GET', 'POST'])
def edit_item(item_id):
    if request.method == 'GET':
        conn = sqlite3.connect('marcenaria.db')
        c = conn.cursor()
        c.execute('SELECT * FROM items WHERE id = ?', (item_id,))
        item = c.fetchone()
        conn.close()
        return render_template('edit.html', item=item)
    elif request.method == 'POST':
        name = request.form['name']
        description = request.form['description']
        quantity = request.form['quantity']
        conn = sqlite3.connect('marcenaria.db')
        c = conn.cursor()
        c.execute('UPDATE items SET name = ?, description = ?, quantity = ? WHERE id = ?', (name, description, quantity, item_id))
        conn.commit()
        conn.close()
        return redirect(url_for('show_items'))

# Rota para deletar um item
@app.route('/delete/<int:item_id>')
def delete_item(item_id):
    conn = sqlite3.connect('marcenaria.db')
    c = conn.cursor()
    c.execute('DELETE FROM items WHERE id = ?', (item_id,))
    conn.commit()
    conn.close()
    return redirect(url_for('show_items'))

# Função principal
if __name__ == '__main__':
    create_table()
    app.run(debug=True)
