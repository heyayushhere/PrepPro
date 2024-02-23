def generate_dynamic_roadmapdsa_data():
    # This function can be extended to generate the roadmap dynamically based on your requirements
    return {
        'nodes': [
            { 'id': 1, 'label': 'Basic Data Structures', 'x': 100, 'y': 100, 'color': '#FFC300' },
{ 'id': 2, 'label': 'Arrays and Strings', 'x': 100, 'y': 150, 'color': '#FFC300' },
{ 'id': 3, 'label': 'Linked Lists', 'x': 100, 'y': 200, 'color': '#FFC300' },
{ 'id': 4, 'label': 'Stacks and Queues', 'x': 100, 'y': 250, 'color': '#FFC300' },
{ 'id': 5, 'label': 'Trees', 'x': 100, 'y': 300, 'color': '#FFC300' },
{ 'id': 6, 'label': 'Graphs', 'x': 100, 'y': 350, 'color': '#FFC300' },
{ 'id': 7, 'label': 'Advanced Data Structures', 'x': 500, 'y': 100, 'color': '#FFC300' },
{ 'id': 8, 'label': 'Heaps', 'x': 500, 'y': 150, 'color': '#FFC300' },
{ 'id': 9, 'label': 'Advanced Trees', 'x': 500, 'y': 200, 'color': '#FFC300' },
{ 'id': 10, 'label': 'Tries', 'x': 500, 'y': 250, 'color': '#FFC300' },
{ 'id': 11, 'label': 'Segment Trees', 'x': 500, 'y': 300, 'color': '#FFC300' },
{ 'id': 12, 'label': 'Hashing', 'x': 500, 'y': 350, 'color': '#FFC300' },
{ 'id': 13, 'label': 'Graph Algorithms', 'x': 500, 'y': 400, 'color': '#FFC300' }
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
