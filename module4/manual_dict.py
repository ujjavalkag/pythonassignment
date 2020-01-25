import pandas as pd
squad={
    'batsman':{'rohit sharma':{'matches':295,
                               'runs':9098,
                               },
               'shikar dhawan':{'matches':200,
                                'runs':6000}
               }
    }
print(pd.DataFrame(squad['batsman']))
