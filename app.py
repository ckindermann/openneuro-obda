from flask import Flask, render_template
import json

app = Flask(__name__)

def assign_ids(node, next_id=0):
    """
    Recursively assign a unique id to each node in the tree.
    """
    node['id'] = next_id
    next_id += 1
    for child in node.get('children', []):
        next_id = assign_ids(child, next_id)
    return next_id

# -----------------------
# Define three example trees
# -----------------------

# Tree 1: Sample tree.
tree1 = {
    "label": "Root",
    "info": [],
    "children": [
        {
            "label": "Folder 1",
            "info": [
                {"label": "File 1-1", "destination": "/destination1-1"},
                {"label": "File 1-2", "destination": "/destination1-2"}
            ],
            "children": [
                {
                    "label": "Subfolder 1-1",
                    "info": [
                        {"label": "File 1-1-1", "destination": "/destination1-1-1"}
                    ],
                    "children": []
                }
            ]
        },
        {
            "label": "Folder 2",
            "info": [
                {"label": "File 2-1", "destination": "/destination2-1"}
            ],
            "children": []
        }
    ]
}
assign_ids(tree1)

# Tree 2: A sample "Home" tree.
tree2 = {
    "label": "Home",
    "info": [],
    "children": [
        {
            "label": "Documents",
            "info": [
                {"label": "Doc1", "destination": "/doc1"}
            ],
            "children": [
                {
                    "label": "Work",
                    "info": [
                        {"label": "Report", "destination": "/report"}
                    ],
                    "children": []
                }
            ]
        },
        {
            "label": "Pictures",
            "info": [
                {"label": "Pic1", "destination": "/pic1"}
            ],
            "children": []
        }
    ]
}
assign_ids(tree2)

# Tree 3: A sample "Media" tree.
tree3 = {
    "label": "Media",
    "info": [],
    "children": [
        {
            "label": "Music",
            "info": [
                {"label": "Song1", "destination": "/song1"},
                {"label": "Song2", "destination": "/song2"}
            ],
            "children": []
        },
        {
            "label": "Videos",
            "info": [
                {"label": "Video1", "destination": "/video1"}
            ],
            "children": []
        }
    ]
}
assign_ids(tree3)

# Bundle the trees in a dictionary.
trees = {
    "Tree 1": tree1,
    "Tree 2": tree2,
    "Tree 3": tree3
}

@app.route('/')
def index():
    return render_template("index.html", trees=trees)

if __name__ == '__main__':
    app.run(debug=True)
