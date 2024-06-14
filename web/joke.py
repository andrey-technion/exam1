from flask import Flask, render_template, request
import requests

app = Flask('mywebapp')

@app.route('/')
def joke():
    try:
        response = requests.get('https://api.chucknorris.io/jokes/random') # {"categories":["dev"],"created_at":"2020-01-05 13:42:19.324003","icon_url":"https://assets.chucknorris.host/img/avatar/chuck-norris.png","id":"o8a2hwedsl229fyvwikkxq","updated_at":"2020-01-05 13:42:19.324003","url":"https://api.chucknorris.io/jokes/o8a2hwedsl229fyvwikkxq","value":"The only pattern Chuck Norris knows is God Object."}
        userDict = response.json()

        joke = userDict['value']

        return f'{joke}'

    except Exception as e:
        return f"An error occurred: {e}"


def main() -> None:
    app.run(port=8001, host="0.0.0.0", debug=True)


if __name__ == '__main__':
    main()