def generate_dynamic_roadmap_data():
    # This function can be extended to generate the roadmap dynamically based on your requirements
    return {
        'nodes': [
             { 'id': 1, 'label': 'Introduction to Python', 'x': 100, 'y': 100, 'color': '#FFC300' },
            { 'id': 2, 'label': 'Data Types and Variables', 'x': 100, 'y': 150, 'color': '#FFC300' },
            { 'id': 3, 'label': 'Control Flow (if, else, elif)', 'x': 100, 'y': 200, 'color': '#FFC300' },
            { 'id': 4, 'label': 'Functions and Modules', 'x': 100, 'y': 250, 'color': '#FFC300' },
            { 'id': 5, 'label': 'Data Structures (Lists, Dictionaries)', 'x': 100, 'y': 300, 'color': '#FFC300' },
            { 'id': 6, 'label': 'File Handling', 'x': 100, 'y': 400, 'color': '#FFC300' },
            { 'id': 7, 'label': 'Exception Handling', 'x': 100, 'y': 450, 'color': '#FFC300' },
            { 'id': 8, 'label': 'Object-Oriented Programming', 'x': 100, 'y': 500, 'color': '#FFC300' },
            { 'id': 9, 'label': 'Testing and Debugging', 'x': 100, 'y': 550, 'color': '#FFC300' },
            { 'id': 10, 'label': 'Web Development (Flask, Django)', 'x': 100, 'y': 600, 'color': '#FFC300' },
            { 'id': 11, 'label': 'Arrays and Linked Lists', 'x': 600, 'y': 300, 'color': '#FFC300' },
            { 'id': 12, 'label': 'Heaps, Stacks, and Queues', 'x': 600, 'y': 350, 'color': '#FFC300' },
            { 'id': 19, 'label': 'Hash Tables', 'x': 600, 'y': 400, 'color': '#FFC300' },
            { 'id': 20, 'label': 'Binary Search Trees', 'x': 600, 'y': 450, 'color': '#FFC300' },
            { 'id': 21, 'label': 'Recursion', 'x': 600, 'y': 500, 'color': '#FFC300' },
            { 'id': 22, 'label': 'Sorting Algorithms', 'x': 600, 'y': 550, 'color': '#FFC300' },
            { 'id': 17, 'label': 'Flask Web Framework', 'x': 400, 'y': 600, 'color': '#FFC300' },
            { 'id': 18, 'label': 'Django Web Framework', 'x': 400, 'y': 650, 'color': '#FFC300' },
        ],
        'edges': [
            { 'from': 1, 'to': 2 },
            { 'from': 2, 'to': 3 },
            { 'from': 3, 'to': 4 },
            { 'from': 2, 'to': 5 },
            { 'from': 5, 'to': 6 },
            { 'from': 3, 'to': 7 },
            { 'from': 4, 'to': 8 },
            { 'from': 7, 'to': 9 },
            { 'from': 8, 'to': 10 },
            { 'from': 5, 'to': 11 },
            { 'from': 11, 'to': 12 },
            { 'from': 12, 'to': 19 },
            { 'from': 19, 'to': 20 },
            { 'from': 20, 'to': 21 },
            { 'from': 21, 'to': 22 },
            { 'from': 10, 'to': 17 },
            { 'from': 17, 'to': 18 },
        ]
    }
