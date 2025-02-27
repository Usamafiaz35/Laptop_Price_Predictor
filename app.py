from flask import Flask, render_template, request
import pickle
import numpy as np
from form import LaptopForm  

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret_key'

# Load model and data
pipe = pickle.load(open('pipe.pkl','rb'))
df = pickle.load(open('df.pkl','rb'))

@app.route("/", methods=["GET", "POST"])
def index():
    form = LaptopForm()
    
    # Choices dynamically set
    form.company.choices = [(c, c) for c in df['Company'].unique()]
    form.type.choices = [(t, t) for t in df['TypeName'].unique()]
    form.cpu.choices = [(c, c) for c in df['Cpu brand'].unique()]
    form.gpu.choices = [(g, g) for g in df['Gpu brand'].unique()]
    form.os.choices = [(o, o) for o in df['os'].unique()]

    price = None
    if request.method == "POST" and form.validate_on_submit():
        touchscreen = int(form.touchscreen.data)
        ips = int(form.ips.data)
        X_res, Y_res = map(int, form.resolution.data.split('x'))
        ppi = ((X_res**2) + (Y_res**2)) ** 0.5 / float(form.screen_size.data)

        query = np.array([
            form.company.data, form.type.data, int(form.ram.data),
            float(form.weight.data), touchscreen, ips, ppi,
            form.cpu.data, int(form.hdd.data), int(form.ssd.data),
            form.gpu.data, form.os.data
        ]).reshape(1, 12)

        price = int(np.exp(pipe.predict(query)[0]))

    return render_template("index.html", form=form, price=price)

if __name__ == "__main__":
    app.run(debug=True)
