from column_transport_parameters import optimization_problem,process,simulator,comparator

from scipy.optimize import minimize
x0=[0.5,0.5]

def loss(x):
    return optimization_problem.evaluate_objectives(x,untransform= True)


res2=minimize(loss,x0,bounds=[(0,1),(0,1)],method="nelder-mead")
#Achtung: Werte hier scheinen sehr schlecht weil wieder transformiert,i.e. use optimisation_problem.untransform
trans_val=optimization_problem.untransform(res2.x)
print(trans_val)

bounds1=[(0.1,0.6),(1e-10,0.1)]
res1=minimize(optimization_problem.evaluate_objectives, x0,method="nelder-mead", bounds=bounds1)
print(res1)

werte1=[ 5.000e-01 ,1.000e-03]
werte2=[  4.122e-01, 2.161e-07]

process.flow_sheet.units_dict["column"].bed_porosity=werte1[0]
process.flow_sheet.units_dict["column"].axial_dispersion=werte1[1]
simulation_results=simulator.simulate(process)
_ = simulation_results.solution.outlet.inlet.plot()
comparator.plot_comparison(simulation_results)


process.flow_sheet.units_dict["column"].bed_porosity=werte2[0]
process.flow_sheet.units_dict["column"].axial_dispersion=werte2[1]
simulation_results=simulator.simulate(process)
_ = simulation_results.solution.outlet.inlet.plot()
comparator.plot_comparison(simulation_results)

process.flow_sheet.units_dict["column"].bed_porosity=trans_val[0]
process.flow_sheet.units_dict["column"].axial_dispersion=trans_val[1]
simulation_results=simulator.simulate(process)
_ = simulation_results.solution.outlet.inlet.plot()
comparator.plot_comparison(simulation_results)


