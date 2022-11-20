import cohere
#3oLDdEpdxqjQLAb1Dy79s48EvYy6cugIb9vpjwpz
co = cohere.Client('3oLDdEpdxqjQLAb1Dy79s48EvYy6cugIb9vpjwpz')
#Prediction
predictresp = input("Enter a prompt to write about: ")
response = co.generate(prompt=predictresp, model='xlarge',  stop_sequences=["--"])
print('Prediction: {}'.format(response.generations[0].text))
