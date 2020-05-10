import pandas as pd

df = pd.read_csv('iris.csv', delimiter = ',')
print(df.groupby('variety').max()[['sepalLength']].to_markdown())

print(df.groupby('variety').sepalLength.agg(
    maxSepalLength  = 'max',
    minSepalLength  = 'min',
    ).to_markdown())
    
print(df.groupby('variety').sepalLength.agg([
    lambda x: x.max(), 
    lambda x: x.min()
    ]).to_markdown())
    
df.groupby('variety').agg(
    maxSepalLength = pd.NamedAgg(column = 'sepalLength', aggfunc = 'max'),
    minSepalLength = pd.NamedAgg(column = 'sepalLength', aggfunc = 'min'),
    maxSepalWidth = pd.NamedAgg(column = 'sepalWidth', aggfunc = 'max'),
    minSepalWidth = pd.NamedAgg(column = 'sepalWidth', aggfunc = 'min'),
    maxPetalLength = pd.NamedAgg(column = 'petalLength', aggfunc = 'max'),
    minPetalLength = pd.NamedAgg(column = 'petalLength', aggfunc = 'min'),
    maxPetalWidth = pd.NamedAgg(column = 'petalWidth', aggfunc = 'max'),
    minPetalWidth = pd.NamedAgg(column = 'petalWidth', aggfunc = 'min'),
    )
    
df.groupby('variety').agg([
    lambda x: x.max(),
    lambda x: x.min()
    ])
    