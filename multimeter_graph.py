from matplotlib import pyplot as plt
import sys

def multimeterplot(filename, output):
    T, PD_V, SSR_V, PD_C, SSR_C = [], [], [], [], []
    for line in open(filename, 'r'):
        values = [float(s) for s in line.split()]
        T.append(values[0])
        PD_V.append(values[1])
        SSR_V.append(values[2])
	PD_C.append(values[3])
	SSR_C.append(values[4])

    figure, axis = plt.subplots(2, constrained_layout=True)

    arrow_dict = dict(arrowstyle="->", color="saddlebrown")
    #voltage-time plot
    axis[0].plot(T, PD_V, color='k', label='PD_V')
    axis[0].plot(T, SSR_V, color='r', label='SSR_V')
    axis[0].set(xlabel = 'time(s)', ylabel = 'voltage(V)', title='voltage')
    
    PD_Vmax = max(PD_V)
    PD_vTpos = PD_V.index(PD_Vmax)
    PD_vTmax = T[PD_vTpos]
    
    SSR_Vmax = max(SSR_V)
    SSR_vTpos = SSR_V.index(SSR_Vmax)
    SSR_vTmax = T[SSR_vTpos]

    #axis[0].annotate(PD_Vmax, xy=(PD_vTmax, PD_Vmax), xytext=(PD_vTmax+30, PD_Vmax), arrowprops=arrow_dict,)
   
    axis[0].plot(PD_vTmax, PD_Vmax, 'ko')
    axis[0].text(PD_vTmax, PD_Vmax, 'PD max:'+str(PD_Vmax))    
    #axis[0].annotate(SSR_Vmax, xy=(SSR_vTmax, SSR_Vmax), xytext=(SSR_vTmax+30, SSR_Vmax), arrowprops=arrow_dict,)
    
    axis[0].plot(SSR_vTmax, SSR_Vmax, 'ro')
    axis[0].text(SSR_vTmax, SSR_Vmax, 'SSR max:'+str(SSR_Vmax))    
    
    PD_Vmin = min(PD_V)
    PD_vTpos = PD_V.index(PD_Vmin)
    PD_vTmin = T[PD_vTpos]
    #axis[0].annotate(PD_Vmin, xy=(PD_vTmin, PD_Vmin), xytext=(PD_vTmin-30, PD_Vmin), arrowprops=arrow_dict,)
    
    axis[0].plot(PD_vTmin, PD_Vmin, 'ko')
    axis[0].text(PD_vTmin, PD_Vmin, 'PD min:'+str(PD_Vmin))    
    
    SSR_Vmin = min(SSR_V)
    SSR_vTpos = SSR_V.index(SSR_Vmin)
    SSR_vTmin = T[SSR_vTpos]
    #axis[0].annotate(SSR_Vmin, xy=(SSR_vTmin, SSR_Vmin), xytext=(SSR_vTmin-30, SSR_Vmin), arrowprops=arrow_dict,)
    
    axis[0].plot(SSR_vTmin, SSR_Vmin, 'ro')
    axis[0].text(SSR_vTmin, SSR_Vmin, 'SSR min:'+str(SSR_Vmin))    
    
    axis[0].legend()
    
    #current-time plot
    axis[1].plot(T, PD_C, color='k', label='PD_C')
    axis[1].plot(T, SSR_C, color='r', label='SSR_C')
    axis[1].set(xlabel = 'time(s)', ylabel = 'current(A)', title='current')

    PD_Cmax = max(PD_C)
    PD_cTpos = PD_C.index(PD_Cmax)
    PD_cTmax = T[PD_cTpos]
    #axis[1].annotate(PD_Cmax, xy=(PD_cTmax, PD_Cmax), xytext=(PD_cTmax+30, PD_Cmax), arrowprops=arrow_dict,)

    axis[1].plot(PD_cTmax, PD_Cmax, 'ko')
    axis[1].text(PD_cTmax, PD_Cmax, 'PD max:'+str(PD_Cmax))    
    
    SSR_Cmax = max(SSR_C)
    SSR_cTpos = SSR_C.index(SSR_Cmax)
    SSR_cTmax = T[SSR_cTpos]
    #axis[1].annotate(SSR_Cmax, xy=(SSR_cTmax, SSR_Cmax), xytext=(SSR_cTmax+30, SSR_Cmax), arrowprops=arrow_dict,)
    
    axis[1].plot(SSR_cTmax, SSR_Cmax, 'ro')
    axis[1].text(SSR_cTmax, SSR_Cmax, 'SSR max:'+str(SSR_Cmax))    
    
    PD_Cmin = min(PD_C)
    PD_cTpos = PD_C.index(PD_Cmin)
    PD_cTmin = T[PD_cTpos]
    #axis[1].annotate(PD_Cmin, xy=(PD_cTmin, PD_Cmin), xytext=(PD_cTmin-30, PD_Cmin), arrowprops=arrow_dict,)
    
    axis[1].plot(PD_cTmin, PD_Cmin, 'ko')
    axis[1].text(PD_cTmin, PD_Cmin, 'PD min:'+str(PD_Cmin))    
    
    SSR_Cmin = min(SSR_C)
    SSR_cTpos = SSR_C.index(SSR_Cmin)
    SSR_cTmin = T[SSR_cTpos]
    #axis[1].annotate(SSR_Cmin, xy=(SSR_cTmin, SSR_Cmin), xytext=(SSR_cTmin-30, SSR_Cmin), arrowprops=arrow_dict,)
    axis[1].plot(SSR_cTmin, SSR_Cmin, 'ro')
    axis[1].text(SSR_cTmin, SSR_Cmin, 'SSR min:'+str(SSR_Cmin))    
    
    axis[1].legend()

    #plt.show()
    plt.savefig(output)

if __name__ == "__main__":
    filename = sys.argv[1]
    output = sys.argv[2]
    multimeterplot(filename, output)
