import math
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Linked List Implementation
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        curr = self.head
        while curr.next:
            curr = curr.next
        curr.next = new_node

    def pop(self):
        if not self.head:
            return None
        if not self.head.next:
            val = self.head.data
            self.head = None
            return val
        curr = self.head
        while curr.next.next:
            curr = curr.next
        val = curr.next.data
        curr.next = None
        return val

    def to_list(self):
        result = []
        curr = self.head
        while curr:
            result.append(curr.data)
            curr = curr.next
        return result

# Single instance para sa session
linked_list_store = LinkedList()

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/profile')
def profile():
    return render_template('profile.html')

@app.route('/area', methods=['GET', 'POST'])
def area():
    circle_area = None
    triangle_area = None
    
    if request.method == 'POST':
        calc_type = request.form.get('calc_type')
        if calc_type == 'circle':
            radius = float(request.form.get('radius', 0))
            circle_area = round(math.pi * (radius ** 2), 2)
        elif calc_type == 'triangle':
            base = float(request.form.get('base', 0))
            height = float(request.form.get('height', 0))
            triangle_area = round(0.5 * base * height, 2)

    return render_template('area.html', circle_area=circle_area, triangle_area=triangle_area)

@app.route('/linked-list', methods=['GET', 'POST'])
def linked_list():
    if request.method == 'POST':
        action = request.form.get('action')
        data = request.form.get('value')
        
        if action == 'append' and data:
            linked_list_store.append(data)
        elif action == 'pop':
            linked_list_store.pop()
            
        return redirect(url_for('linked_list'))

    items = linked_list_store.to_list()
    # Pinalitan mula 'linked_list.html' patungong 'Linked_List.html' para mag-match sa file mo sa templates/ folder!
    return render_template('Linked_List.html', items=items)

if __name__ == '__main__':
    app.run(debug=True)
