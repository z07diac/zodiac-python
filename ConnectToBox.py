from boxsdk import JWTAuth
from boxsdk import Client

# Configure JWT auth object
sdk = JWTAuth(
  client_id="xx",
  client_secret="xx",
  enterprise_id="xx",
  jwt_key_id="xx",
  rsa_private_key_file_sys_path="/xx/private_key_product.cfg",
  rsa_private_key_passphrase="xx",
)


# Get auth client
client = Client(sdk)
ev_user=client.user(user_id='xx')
sdk.authenticate_app_user(ev_user)
ev_client = Client(sdk)
# PERFORM API ACTIONS WITH CLIENT

root_folder = ev_client.folder(folder_id='xx')
#shared_folder = root_folder.create_subfolder('shared_folder_xx')
uploaded_file = root_folder.upload('LocalTestUrl.html')
#shared_link = shared_folder.get_shared_link()