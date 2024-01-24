from flask import Flask, render_template, request
from image_processor import process_image
# from chat_cat import chat_with_gpt


app = Flask(__name__)


@app.route("/")
def hello_world():
    return render_template('index.html')


@app.route('/img', methods=["GET", "POST"])
def predict_img():
    if request.method == 'POST':
        # Get the URL from the form
        # url = request.form['url']
        uploaded_file = request.files['fileInput']
        if uploaded_file.filename != '':
            image_path = 'static/results.jpg'
            uploaded_file.save(image_path)
            image_results, output = process_image(image_path)

            # Use output to determine if polyp is detected or not
            result = 'Result: Polyp Not-detected'

            print(image_results, result)
            return render_template('index.html', results=image_results, output=result)
        return 'Error in uploading file'

        # Set the image_url variable for displaying in the template
        # image_url = url

        # Process the image using YOLO (replace with your YOLO code)
    #     image_results, output = process_image(image_path)
    #     print(image_results, output)
    #
    # return render_template('index.html', results=image_results)


# @app.route('/chat', methods=["POST"])
# def chatgpt():
#     if request.method == 'POST':
#         chat = request.form['chat']
#         chat_response = chat_with_gpt(chat)
#         return render_template('index.html', reply=chat_response, user=chat)


if __name__ == '__main__':
    app.run(debug=True)
