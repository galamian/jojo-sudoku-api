# Copyright 2018 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# [START gae_python37_app]
from flask import Flask, request, jsonify, Response
from flask import make_response
from sudoku.sudoku import Sudoku


# If `entrypoint` is not defined in app.yaml, App Engine will look for an app
# called `app` in `main.py`.
app = Flask(__name__)


@app.route('/api/solve', methods = ['GET', 'POST'])
def solve():

    """puzzle = [[5,3,0,0,7,0,0,0,0],
                [6,0,0,1,9,5,0,0,0],
                [0,9,8,0,0,0,0,6,0],
                [8,0,0,0,6,0,0,0,3],
                [4,0,0,8,0,3,0,0,1],
                [7,0,0,0,2,0,0,0,6],
                [0,6,0,0,0,0,2,8,0],
                [0,0,0,4,1,9,0,0,5],
                [0,0,0,0,8,0,0,7,9]]"""
    """puzzle = [[0,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0]]"""

    if request.method == 'POST':  # this block is only entered when the form is submitted
        input = request.form['sudoku']        
        size = request.form['size']
    elif request.method == 'GET':
        input = request.args.get('sudoku')
        size = request.args.get('size')
    else: 
        pass


    if size != None and size != '':
        try:
            size = int(size)
        except ValueError:
            size = 9
    else:
        size = 9


    sud = Sudoku(input, size)
    # if input != None and input != '':
    #     puzzle = string_to_matrix(input, size)
    # else:
    #     puzzle = string_to_matrix('0', size)
        # for i in range(len(param)):
        #         puzzle[i//9][i%9]=int(param[i])
    
    
    #solution = sudoku(puzzle)
    solution = sud.solve()
    conArray = sum([solution[i] for i in range(len(solution))], [])
    returnString = ''.join([str(x) for x in conArray])

    #resp = Response(jsonify({'sudoku': solution}))
    #resp = make_response(solution)
    #resp.headers['Access-Control-Allow-Origin'] = '*'
    #resp.data = solution
    #return jsonify({'sudoku': solution})
    #return Response(jsonify({'sudoku': solution, 'headers': {'Access-Control-Allow-Origin':'*'} }))
    #return Response(message=jsonify({'sudoku': solution}), headers={'Access-Control-Allow-Origin':'*'})

    resp = make_response(jsonify({'sudoku': returnString}))
    resp.headers['Access-Control-Allow-Origin'] = '*'
    return resp
    


"""def solve(puzzle):
    sol = sudoku(puzzle)
    print(sol)
    str(sol)"""
    

@app.route('/api')
def hello():
    """Return a friendly HTTP greeting."""
    return 'Hello World!'


if __name__ == '__main__':
    # This is used when running locally only. When deploying to Google App
    # Engine, a webserver process such as Gunicorn will serve the app. This
    # can be configured by adding an `entrypoint` to app.yaml.
    app.run(host='127.0.0.1', port=8080, debug=True)
# [END gae_python37_app]