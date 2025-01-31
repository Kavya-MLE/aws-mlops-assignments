from flask import Flask, jsonify, request
import boto3

app = Flask(__name__)

@app.route('/list_objects', methods=['GET'])
def list_files():
    bucket_name = "tiger-mle-pg"  # Replace with your actual bucket name
    folder_name = "home/kavya.konakati/"

    if not folder_name:
        return jsonify({"error": "Missing 'folder' parameter"}), 400

    session = boto3.Session(profile_name="pe-mle-user-role")  # Use the correct profile
    s3 = session.client('s3')

    try:
        response = s3.list_objects_v2(Bucket=bucket_name, Prefix=folder_name)
        print("response!!!!!", response)
        if 'Contents' in response:
            files = [obj['Key'] for obj in response['Contents']]
            return jsonify({"files": files})
        else:
            return jsonify({"message": f"No files found under '{folder_name}' in '{bucket_name}'."})

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8085)