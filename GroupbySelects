select
	i.Variety 
	,max(i.SepalLength) as maxSepalLength 
	,min(i.SepalLength) as minSepalLength
	,max(i.SepalWidth) as maxSepalWidth
	,min(i.SepalWidth) as minSepalWidth
	,max(i.PetalLength) as maxPetalLength
	,min(i.PetalLength) as mibPetalLength
	,max(i.PetalWidth) as maxPetalWidth
	,min(i.PetalWidth) as minPetalWidth
from Iris i
	group by i.Variety
	
	
select i.Variety, max(i.SepalLength) as maxSepalLength
	from Iris i
		group by i.Variety