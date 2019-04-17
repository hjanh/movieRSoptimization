from scipy.optimize import minimize
import numpy as np

    def optimize_weights(users):
    
        obj_func = lambda w, data: np.sum(abs(data[2, :] 
        - (data[0, :] * w[0] + data[1, :] * w[1])) 

        for uid, user in users.iteritems():
            res = minimize(obj_func, [1,0], args=user, bounds=[(0,1),(0,1)] ,
                           constraints=[{'type':'eq', 'fun': lambda w: w[0]+w[1]-1},
                           {'type':'ineq', 'fun': lambda w: w[0]-w[1]}])
            weights[uid].append(res.x)
            
        return weights
        
