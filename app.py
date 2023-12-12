from flask import Flask , render_template ,jsonify

app = Flask(__name__)

JOBS= [
  {
    'id':1,
    'title': 'Data Analyste',
    'location': 'Bengarlu , India',
    'salary' : ' RS. 10000'
    
  },
  {
    'id':2,
    'title': 'Data Scientist',
    'location': 'Remote'
  },
{
  'id':3,
  'title': 'Data Engineer',
  'location': 'Bengarlu , India',
  'salary' : ' RS. 13000'
},
{
  'id':4,
  'title': 'BackEnd Engineer ',
  'location': 'San Fransisco  , USA',
  'salary' : ' $120000'
}
      ]

@app.route("/")
def hello_jovian():
  return render_template('home.html',jobs=JOBS,company_name='Jovian')

@app.route("/jobs")
def list_jobs():
  return jsonify(JOBS)

if __name__ == "__main__":
  app.run(host="0.0.0.0", debug=True)
