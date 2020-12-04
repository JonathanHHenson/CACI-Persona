from flask import jsonify


def jsonify_list(model_list):
    """Serializes a list of SerializerMixin objects

    :param model_list: a list of SerializerMixin objects
    :return: a list of JSON objects
    """
    result = list(map(lambda c: c.to_dict(), model_list))
    return jsonify(result)


def jsonify_one(model):
    """Serializes a SerializerMixin object

    :param model: a SerializerMixin object
    :return: a JSON object
    """
    return jsonify(model.to_dict())
