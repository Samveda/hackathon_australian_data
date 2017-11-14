# Develop​ ​a​ ​model​ ​to​ ​deny​ ​or​ ​approve​ ​Credit​ ​Card​ ​Application

## Statlog (Australian Credit Approval) Data Set 

### Problem​ ​Statement: 
Develop​ ​a​ ​predictive​ ​model​ ​to​ ​approve​ ​or​ ​deny​ ​an​ ​Credit​ ​card​ ​application. Some​ ​Research​ ​Questions 
- 1. Is​ ​there​ ​a​ ​correlation​ ​between​ ​Age,​ ​Income,​ ​Credit​ ​Score,​ ​and​ ​Debt​ ​levels​ ​and​ ​the​ ​credit approval​ ​status?​ ​Can​ ​this​ ​relationship​ ​be​ ​used​ ​to​ ​predict​ ​if​ ​a​ ​person​ ​is​ ​granted​ ​credit?​ ​If​ ​yes, does​ ​the​ ​relationship​ ​indicate​ ​reasonable​ ​risk​ ​management​ ​strategies? 
- 2. Ethnicity​ ​is​ ​a​ ​protected​ ​status​ ​and​ ​the​ ​decision​ ​to​ ​approve​ ​or​ ​deny​ ​an​ ​application​ ​cannot​ ​be based​ ​on​ ​the​ ​applicant’s​ ​ethnicity.​ ​Is​ ​there​ ​a​ ​statistically​ ​significant​ ​difference​ ​in​ ​how​ ​credit​ ​is granted​ ​between​ ​ethnicities​ ​that​ ​could​ ​indicate​ ​bias​ ​or​ ​discrimination?​ ​Contrarily,​ ​could​ ​the difference​ ​indicate​ ​a​ ​business​ ​opportunity? 



| Data​ ​Set Characteristics:  | Multivariate | Number​ ​of Instances: | 690 | Area: | Financial  |
| :---: | :---: |:---: | :---: | :---: | :---: |
| Attribute Characteristics:  | Categorical,​ ​Integer, Real | Number​ ​of Attributes: | 14 | Date Donated | N/A |
| Associated​ ​Tasks: | Classification | Missing​ ​Values? | Yes | Number​ ​of​ ​Web Hits: | 98429 |

### Data​ ​Set​ ​Information: 
This​ ​file​ ​concerns​ ​credit​ ​card​ ​applications.​ ​All​ ​attribute​ ​names​ ​and​ ​values​ ​have​ ​been​ ​changed​ ​to​ ​meaningless symbols​ ​to​ ​protect​ ​confidentiality​ ​of​ ​the​ ​data.
   
This​ ​dataset​ ​is​ ​interesting​ ​because​ ​there​ ​is​ ​a​ ​good​ ​mix​ ​of​ ​attributes​ ​--​ ​continuous,​ ​nominal​ ​with​ ​small​ ​numbers​ ​of values,​ ​and​ ​nominal​ ​with​ ​larger​ ​numbers​ ​of​ ​values.​ ​There​ ​are​ ​also​ ​a​ ​few​ ​missing​ ​values.   

### Attribute Information:

There are 6 numerical and 8 categorical attributes. The labels have been changed for the convenience of the statistical algorithms. For example, attribute 4 originally had 3 labels p,g,gg and these have been changed to labels 1,2,3. 

A1: 0,1 CATEGORICAL (formerly: a,b) 
A2: continuous. 
A3: continuous. 
A4: 1,2,3 CATEGORICAL (formerly: p,g,gg) 
A5: 1, 2,3,4,5, 6,7,8,9,10,11,12,13,14 CATEGORICAL (formerly: ff,d,i,k,j,aa,m,c,w, e, q, r,cc, x) 
A6: 1, 2,3, 4,5,6,7,8,9 CATEGORICAL (formerly: ff,dd,j,bb,v,n,o,h,z) 
A7: continuous. 
A8: 1, 0 CATEGORICAL (formerly: t, f) 
A9: 1, 0	CATEGORICAL (formerly: t, f) 
A10: continuous. 
A11: 1, 0	CATEGORICAL (formerly t, f) 
A12: 1, 2, 3 CATEGORICAL (formerly: s, g, p) 
A13: continuous. 
A14: continuous. 
A15: 1,2 class attribute (formerly: +,-)



### Sources: http://archive.ics.uci.edu/ml/datasets/statlog+(australian+credit+approval) 
