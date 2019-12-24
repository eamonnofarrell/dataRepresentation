from flask import Flask, jsonify, request, abort

from phoneDAO import phoneDAO

app = Flask(__name__, static_url_path='', static_folder='.')



@app.route('/phones')
def getAll():
    # print("in getall")

    results = phoneDAO.getAll()

    return jsonify(results)


# curl "http://127.0.0.1:5000/phones/1"

@app.route('/phones/<int:id>')
def findById(id):
    foundPhone = phoneDAO.findByID(id)

    return jsonify(foundPhone)


# curl  -i -H "Content-Type:application/json" -X POST -d "{\"Make\":\"Nokia\",\"Model\":\"Latest1\",\"Price\":130}" http://127.0.0.1:5000/phones

@app.route('/phones', methods=['POST'])
def create():
    if not request.json:
        abort(400)

    # other checking

    phone = {
        "Make": request.json['Make'],
        "Model": request.json['Model'],
        "Price": request.json['Price'],
    }
    values = (phone['Make'], phone['Model'], phone['Price'])
    newId = phoneDAO.create(values)
    phone['id'] = newId
    return jsonify(phone)


# curl  -i -H "Content-Type:application/json" -X PUT -d "{\"Make\":\"Nokia\",\"Model\":\"Latest1\",\"Price\":133}" http://127.0.0.1:5000/phones/1

@app.route('/phones/<int:id>', methods=['PUT'])
def update(id):
    foundPhone = phoneDAO.findByID(id)
    if not foundPhone:
        abort(404)
    if not request.json:
        abort(400)
    reqJson = request.json
    if 'Price' in reqJson and type(reqJson['Price']) is not int:
        abort(400)
    if 'Make' in reqJson:
        foundPhone['Make'] = reqJson['Make']
    if 'Model' in reqJson:
        foundPhone['Model'] = reqJson['Model']
    if 'Price' in reqJson:
        foundPhone['Price'] = reqJson['Price']
    values = (foundPhone['Make'], foundPhone['Model'], foundPhone['Price'], foundPhone['id'])
    phoneDAO.update(values)
    return jsonify(foundPhone)

#  curl -X DELETE "http://127.0.0.1:5000/phones/11"

@app.route('/phones/<int:id>', methods=['DELETE'])
def delete(id):
    phoneDAO.delete(id)
    return jsonify({"done": True})


if __name__ == '__main__' :

    app.run(debug= True)