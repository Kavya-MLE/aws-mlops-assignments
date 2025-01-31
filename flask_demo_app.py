# from flask import Flask
# import boto3
# import time
# app = Flask(__name__)

# @app.route('/name')
# def get_name():
#     return 'AWS MASTERCHEF'

# @app.route('/version')
# def get_version():
#     return 'vl.0.0'

# Retrieve the list of existing buckets

# if __name__ == '__main__':
#     app.run(host='0.0.0.0', port=8000)

# import boto3

# def list_objects_in_prefix(bucket_name, prefix):
#     session = boto3.Session(profile_name="pe-mle-user-role")  # Use the correct profile
#     s3 = session.client('s3')

#     try:
#         response = s3.list_objects_v2(Bucket=bucket_name, Prefix=prefix)

#         if 'Contents' in response:
#             print(f"Objects in '{prefix}' of bucket '{bucket_name}':")
#             for obj in response['Contents']:
#                 print(obj['Key'])  # Print file paths
#         else:
#             print(f"No objects found under '{prefix}' in '{bucket_name}'.")

#     except Exception as e:
#         print(f"Error: {e}")

# # Set your bucket name and folder (prefix)
# bucket_name = "tiger-mle-pg"
# prefix = "home/kavya.konakati/"  # Make sure to include the trailing slash



# if __name__ == "__main__":
#     list_objects_in_prefix(bucket_name, prefix)


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

        if 'Contents' in response:
            files = [obj['Key'] for obj in response['Contents']]
            return jsonify({"files": files})
        else:
            return jsonify({"message": f"No files found under '{folder_name}' in '{bucket_name}'."})

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)