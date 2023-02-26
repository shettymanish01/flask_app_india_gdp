from flask import Flask, render_template, request, redirect, session
from .utility_functions import get_gdp_data, get_host_and_ip



app=Flask(__name__,  static_folder='')



@app.route('/')
@app.route('/India_gdp',methods=['POST', 'GET'])
def index():
    currency = 'U.S. dollars'
    currency_type = request.args.get('currency')
    if currency_type == 'INR' :
        currency = 'Indian Rs'
    elif currency_type != None:
        return redirect("/", code=302)
    data = get_gdp_data(currency)
    return render_template('India_gdp.html',data=data, currency = currency, currency_type=currency_type)

@app.route('/health')
def health():
    host,ip=get_host_and_ip()
    return render_template('health.html',HOST=host, IP = ip)

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'),404


@app.errorhandler(500)
def server_error(e):
    return render_template('500.html'),500



if __name__ == '__main__':
    app.run(debug=True)
    # get_data('Indian Rs')