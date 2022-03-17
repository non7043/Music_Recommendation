from application import app


if __name__ == '__main__':
	app.run(debug=True)

with open("secret.txt") as f:
    secret_ls = f.readlines()
    cid = secret_ls[0][:-2]
    secret = secret_ls[1]