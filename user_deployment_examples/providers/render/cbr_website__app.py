
def main():
    from cbr_website_beta.flask.Flask_Site import Flask_Site

    flask_site = Flask_Site()
    app = flask_site.app()
    app.run(host="0.0.0.0", port=5000)

if __name__ == "__main__":
    main()