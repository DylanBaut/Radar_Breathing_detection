from sense_hat import SenseHat
from time import sleep

sense=SenseHat()

import socket

red = [255, 0, 0]
blue= [0, 0, 255]
def show(inh, exh):
    hue = 0
    sense.clear()
    currTime=0
    flash = False
    for i in range(len(inh)):
        sense.set_pixels([red]*64)
        print(inh[i] - currTime)
        if inh[i] - currTime > 15:
            flash = True
            sleep(15)
            break
        sleep(inh[i]-currTime)
        currTime=inh[i]
        sense.set_pixels([blue]*64)
        if exh[i] - currTime > 15:
            flash = True
            sleep(15)
            break
        sleep(exh[i]-currTime)
        currTime=exh[i]
        
    if flash:
        print('entered')
        sense.clear()
        sense.set_pixels([(255, 255, 0)] * 64)
        
        message = 'Stopped breathing'
        ip_addr = '10.193.53.196'
        port_num = 5000
        
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        sock.sendto(bytes(message, "utf-8"), (ip_addr, port_num))
        
        
       



#####
# import required libraries
sense.clear()
import struct

import sys

import serial

import binascii

import time

import numpy as np

import math

 

import os

import datetime

import matplotlib.pyplot as plt

#/Users/djbautista/Desktop/437/radar/data_12_01_2023_17_52_47.npy

rawData = np.load("/home/pi/Downloads/data_12_01_2023_17_52_47.npy")

data = np.array([frame["adcSamples"][:, 128:] for frame in rawData])

data.shape # chirp* rx * samples per chirp

#########

rangeData = np.fft.fftn(data, axes=(2,))

closest=rangeData[:,:,1]

rangeDoppler = np.fft.fftn(closest, axes=(0,))

doppler=rangeDoppler[:,0]

angles = np.angle(doppler)

window_size=30

inhales = [1.5, 7.1, 9.8, 19.04, 28.4, 35.79]
exhales= [3.1, 200, 12.6, 23.9, 33.5, 37.2]
 

closest1 = rangeData[:,:,2]

rangeDoppler2 = np.fft.fftn(closest1, axes=(0,))

doppler2=rangeDoppler2[:,0]

angles2 = np.angle(doppler2)

cumsum2= np.cumsum(np.insert(angles2,0,0))

smoothed_data2=(cumsum2[window_size:]-cumsum2[:-window_size])/float(window_size)

 

cumsum= np.cumsum(np.insert(angles,0,0))

smoothed_data=(cumsum[window_size:]-cumsum[:-window_size])/float(window_size)

 


#############

import numpy as np

from scipy.signal import find_peaks

import matplotlib.pyplot as plt

 

def calculate_breathing_rate(inhale_peaks, time_per_sample):

    # Calculate time differences between consecutive inhales

    inhale_times = inhale_peaks * time_per_sample

    inhale_time_diff = np.diff(inhale_times)

 

    # Calculate breathing rate (breaths per minute)

    breathing_rate = 60 / np.mean(inhale_time_diff)

 

    return breathing_rate

data = np.array([0.6933923459739726, 0.4096725664609156, 1.9481544398985293, 1.2322925902627893, 1.5642215959781511, 1.0577799106200656, 1.4711236276182653, 1.4154942040581657, 1.7290785244962568, 1.8056041485203218, 1.5321357184466553, 2.0946917267905207, 2.2910279681388976, 1.4861610492800919, 1.2708354180010315, 2.6984393696103326, 1.043618114123317, 1.3399584522844858, 2.4169244539131474, 1.7433066795048282, 1.0529674923322165, 1.3995555270661806, 0.7098722917538282, 1.48453091657081, 0.911123056808304, 1.0123551329923386, 0.4949886637358162, 0.03808769218283922, -0.30258635830105945, -0.5724838185381458, 0.4604208400902525, -0.4797097464286057, -0.6470861219971612, -0.29028759508072377, -0.9590178656011469, -1.205969741970811, -1.8144273301510792, -2.6156781383901357, -2.7284717735102717, -0.8075902755051713, -2.268249580883523, -1.2343108288569065, -1.9352086780729443, -2.305575910472348, -1.7651420783003822, -1.9272621482849628, -2.4225255531175045, -0.5799649737317273, -1.5819788342788046, -0.365773775697693, -1.2822297893144885, -0.9458444703625033, -0.9203775509247438, -0.14728539330078372, 0.006411217530875257, -0.2686624634373088, 0.4555194388277828, 0.0800152274266602, 0.06828761264772025, 0.4450863414847976, -0.6598931193289707, -0.28650567557685136, 0.6797280060104729, 0.45485394140168445, 1.3204226882337287, 1.4419141225049663, -0.09485443241584712, 0.6692064062478904, 1.032793046522818, 0.8573477219806368, 0.3775119848465741, 1.7667436565017383, 0.7751105696554685, 0.8929882443105938, 0.09170019092364312, 1.0387621017221278, 1.233655613753141, -0.06543106780546454, 0.343432114409859, -0.2482927944004577, 0.8390590623992273, 0.19966315355694458, 1.1491442766437663, 0.9239079445668053, 1.8693468290342559, 2.758008973690225, 2.7570915007704713, 1.6996273171994565, 0.866477877054327, 2.8504842770273937, 1.224980391727229, 1.472578550824077, 0.7395945739560756, 1.7782400527205366, 2.3306508899021963, 1.1428909957588853, 1.0021640812682506, 1.3289964965237608, 0.8808916452547866, 1.3745358292263972, 1.5061509206270365, 1.336421791340388, 1.8802384425390937, 1.2138681547033874, 1.3270324298359757, 0.8181362800329884, 0.058922961492535786, 1.1446160393807499, 1.3875740958012541, -0.5305904233016259, -0.26377627270961784, 0.8219329207484288, -0.3739740261091072, 0.7898468541124581, 0.3313475700807146, 0.5003296304064123, -0.019621823066214197, -0.934561160026423, 0.38843941442904606, 0.7304643877477661, 0.5942410314167915, -0.278232081782119, -0.5354345881489526, -0.7274186222504679, -0.27697694938746975, -0.5514202491708677, 0.6409802258309818, 0.4667374015620314, -1.1437552412483567, 1.395532495228603, -0.10226688879473567, 1.1259332373338502, 0.3759709191349238, -0.29669996380214303, 0.9121016867449179, 1.6050572561208156, 0.820606788827193, 1.1198457692501407, 1.5854246443599083, 0.5427197085191526, 1.36901907728501, 2.298110217645874, 1.3680203232339176, 2.2223636818779986, 1.6146578131136904, 2.496396800834272, 1.929787030328805, 1.1240189124026303, 2.001060614721163, 2.910433084947969, 2.784590334104969, 2.68781533705742, 2.477756311830999, 2.5855078044263218, 3.0260594928858024, 3.3714390431319488, 2.3439560665266894, 2.1408214386110878, 2.3422055375487103, 2.1945932690973993, 2.261484604559523, 2.281563044613708, 1.8927656434603728, 2.547017932512089, 2.641015103339246, 2.016702546804512, 1.738344386733962, 1.506664353529895, 1.9021231978226838, 0.026539471459519633, -0.01476548968183133, 0.03504506790993088, 0.17050296528430386, -0.14346346002625004, 0.032007778761675244, -0.01849906384222067, -0.14327597954005172, -0.020220176111245, -0.0850702177683913, -0.00878058479730516, 0.03904045983727743, 0.010869852526943155, -0.08025565660756882, 0.01460454128623534, 0.007932220046209276, 0.06168489233627646, 0.06394574965259864, 0.1802653103077402, 0.12124507496966605, 0.17182206023174143, 0.1076927664465849, 0.052804940534568204, 0.071426146251394, 0.1842160539687139, 0.2287846283924152, 0.14804028218589482, 0.13693638332868702, 0.11139414674532644, 0.09075966948012423, 0.14620811539319836, 0.12195643127908987, 0.03412441148205126, 0.010831982481423287, 0.019353308798272205, 0.10335104781780793, 0.03392470072788325, -0.031885283894438364, 0.02573416949763763, -0.018752960405671492, -0.016273261238739546, 0.02279119453304025, -0.02573626780570229, 0.004916680297437956, 0.007103919610902346, -0.011663639222508605, 0.039587587762068686, 0.011949572020118761, 0.027811601065118707, 0.017995849568944778, -0.06879662342229906, -0.00027010373101171714, 0.15887773463213908, 0.0842044717287172, 0.12745474979674515, 0.07775761800785251, -0.020022339233378858, 0.08046524288666325, 0.001286584042015447, 0.10965687967891508, 0.03135122214645836, 0.01712751668571383, -0.0377240174545521, 0.08154102513333283, -0.04094318473383055, -0.1815930807454501, -0.12228270481416748, -0.02156325944174249, -0.10266332053260321, -0.06640955270305121, -0.04010779118887725, -0.1412898510291725, -0.05210197907621948, -0.1657306288083987, -0.1707913246395948, -0.21315547756026298, -0.1248619376854949, -0.10264994915089072, -0.03316901608544817, 0.1391128427178325, 0.13772957787741064, -0.03415681651324916, 0.06365403080779179, -0.036471866386431545, 0.11680731868500827, 0.2093187718989856, 0.035103075709083616, -0.06475320817395988, 0.07155699208512481, 0.29881807446735575, 0.16212414423720675, 0.04561615882326088, 0.28802218965722254, -0.0533170464367103, 0.11886635558014685, 0.16394242168867557, 0.030672778725993097, 0.09844506355229957, 0.1777674967390337, 0.16559078115266812, 0.10467367972836956, 0.09174602602035785, 0.04672869839510248, 0.09522155535017579, -0.08487636623545608, 0.23521773309266947, -0.008613550535543621, -0.10736978456101925, 0.0008450777258574987, 0.0630574440653371, -0.0880251343281585, -0.030745737074858667, 0.12409467729836421, -0.036573781646417086, 0.0553480424047641, -0.05642015904645456, 0.07117466376564602, -0.08565907408521706, -0.06827692425095563, 0.02912505354570792, -0.07840781167911509, -0.10883218272326202, -0.01597715839277654, -0.1099656672110079, -0.05892074171379419, -0.03488421233445527, -0.24533820125728834, -0.12563706034070465, -0.0898937084627802, -0.2087337361929616, -0.1364272780566515, -0.11051754230682292, -0.003057706424344442, -0.18719978628579698, -0.2434190540663394, -0.1029070518025647, -0.13439707894036726, -0.1503461288699977, -0.043907077337903486, -0.13143646192393205, 0.012870404360649443, -0.07599176878760577, 0.06313061605958728, 0.02768699366865056, -0.03706492405262716, 0.006664784633537726, -0.03243452152610122, -0.19086570289474364, -0.16646649326123514, 0.07037670832612408, 0.10279606964814188, -0.019502867741315405, 0.006425841877666344, 0.09077208036979453, 0.19082536912824052, 0.08702492277637898, 0.14696317444565865, 0.08901035577283604, 0.15475918044380393, 0.09555117108479702, 0.0563536245141773, 0.045422412172823154, 0.20320708533691448, -0.2074011241283435, -0.037036730169387924, -0.05038283772146365, -0.07331066004902047, -0.002602184463704686, 0.005100767573376963, -0.05665636313319036, -0.03578646266500148, -0.14789119258696726, 0.19235232875145986, 0.03406308293079048, 0.01056304368135717, 0.005919661373374199, 0.10421769041811571, 0.08751420646652107, 0.10598302419241983, 0.06671918628134357, 0.08210852136214779, 0.25668340972682835, 0.021787244178343962, 0.13328952662141252, 0.2659787634512269, 0.03777334262245169, 0.11331208563987372, 0.20552060695213734, 0.18700284072493156, 0.07202477349422332, 0.10778833812180443, 0.1594933312233828, 0.11404914446675804, 0.1479338081552528, 0.06575440385411851, -0.11030408750464658, 0.022227468515718517, 0.08719287540683945, -0.08715740692916137, 0.053862584760637315, 0.05724421950378809, -0.08075501820306812, -0.01736013303110441, 0.0659661580225264, 0.02821087005044359, -0.03568457106142406, -0.04150420277374549, 0.20784946571940235, 0.103474478943196, 0.08243236054117264, -0.06654586812413237, 0.14291147466731832, -0.018147163619330026, 0.13376351356255667, 0.17172271574478276, 0.14025395048580228, 0.12826040837333164, 0.26310581289929125, 0.2784733591326775, 0.08823049867995406, 0.4098690681556118, 0.19367604432970362, 0.13578082924128343, 0.12345041727691639, 0.18054802340333054, 0.14139696221907316, -0.06589046196505309, 0.09951580465268936, -0.007269035254004817, -0.14282006535148467, 0.029365505022414147, 0.0915956559476733, -0.2635420217699386, 0.19706078545196334, -0.04441915686986516, -0.05628882345853591, -0.2558581053037352, -0.16285383972305847, -0.19113941620218078, -0.21713187030779926, -0.20789258555617543, -0.11833049724870992, 0.02478362358015635, 0.10677343307756423, -0.030532064762721498, -0.09152741671834261, 0.2156513305831561, 0.1142588172323593, -0.046669898339020466, -0.12042671119111735, -0.04104055934173174, -0.0479233827371003, 0.031083115454322702, 0.10833789083052259, 0.15795660781359522, 0.06787803727668897, 0.09591514464549604, 0.18064446201027284, 0.14127281468699637, 0.13296818983828515, 0.09380483251945727, -0.01790870970614447, 0.1487379377390826, 0.06388601645301897, 0.13958054457549224, 0.024937055893665544, -0.007172591921880536, 0.07142536075694489, 0.16543102644079083, 0.03152619488746136, -0.01602175911690097, 0.0664195654909055, 0.029042396225806646, 0.002758009434628202, 0.054320998111659385, -0.12987971995430783, 0.026697658256186148, -0.08818561064710949, 0.012834624889516748, -0.025333254962641397, -0.005214403591094065, -0.03295161572325821, 0.05322245011796229, 0.00046341171147830373, 0.04364151885152952, 0.027314808008263605, 0.12311608566187618, 0.044529339151781075, 0.10727008539366265, 0.0796623164565505, 0.112860532441009, 0.07448015250508995, 0.04734877026799396, 0.12545305042483484, 0.13367014904948624, 0.1877803379970375, 0.23661063944425387, 0.12692342635802664, 0.24019833096373827, 0.22999810618231062, 0.1332606211733874, 0.1884099716425957, 0.06538374820143594, 0.04852556318231742, 0.07272642469916116, 0.1383967968868715, 0.06937818891292008, 0.08106714321985094, 0.025885848606075373, 0.05229805960872984, 0.0748501477761829, 0.06114168476999839, 0.044244172407573154, -0.0838780597614413, -0.018722051685388694, -0.05000127535006645, -0.08442821999017597, -0.07535041452610311, -0.13262877912020873, -0.12299364890419548, -0.11462523751924837, 0.008281043942828241, 0.00754451580904875, -0.08432234429022845, 0.08103911727138594, 0.021321727777887864, 0.16441668780839308, -0.03325870042420151, -0.010744088015576497, 0.05438705278319207, 0.04283019265392764, 0.028393757168981237, 0.02883895632442996, 0.07695322199356296, 0.22122360810681047, 0.05370616731684582, 0.17934817470322947, 0.08950612245650681, 0.05359975854469709, 0.12467211074934953, 0.2824937737595631, 0.07740311992598634, 0.13930598472006647, 0.08991924771224327, 0.14615097799371518, 0.04266164026276213, 0.1317240047651515, 0.042314089386082804, 0.134613731213843, 0.1042121063397648, 0.03948016642992014, -0.03818338113330877, -0.012219856594675352, 0.06997705441124566, 0.051416449996438435, 0.044512534758984514, -0.04767574701501529, -0.031364122863062005, -0.03309212601539169, 0.038461908599473224, -0.08705043785079596, 0.13835355258871804, 0.06126987913129098, 0.07337851471092538, 0.15405496853021272, 0.06387404654151307, -0.012655802541873706, 0.18942157798122825, 0.05233736734238292, 0.03157432085125693, 0.09619368262789735, 0.08061109959192397, 0.1487922020906401, 0.17228493865291195, 0.23231989317014412, 0.1654934082640327, 0.10456178244696945, 0.15237073659152772, 0.09999058289326132, 0.18071985102770477, 0.1493091914249724, 0.07318855076578676, 0.07971996187285105, 0.06238410904639515, 0.08000593532811515, 0.145864567980368, -0.06795461490289455, 0.03554260046103891, -0.07867371538308082, 0.04721765062241129, -0.05139978291684416, -0.07118685261800846, -0.03931900593859598, -0.07205216222407505, -0.030878996273036016, -0.15072721705610398, -0.12744998780129446, 0.022269295343740697, -0.1578076978303848, 0.030455217247027835, -0.11514538933672125, -0.09221367806604094, -0.09783752933760367, -0.03598772153637912, 0.1017248803018543, 0.10083988688075944, -0.005918755991329246, 0.015429868062269585, -0.021425131721193008, -0.021481735786042868, 0.12673419599660918, -0.032460408909777985, 0.04459360228497565, -0.03672856659408553, -0.005987712727492099, -0.0067156462126698735, 0.04047153268738543, 0.07033647006938, -0.06535098623889941, 0.024499970935321757, -0.03651295273156507, -0.025588075089711438, 0.05124189069640099, -0.006794667286401812, -0.059165802954472754, -0.04905926457014173, 0.05969741148183253, -0.04402222167755388, 0.035475985997095213, -0.037165996586750516, 0.02336500872215324, -0.0022287881804025945, -0.026416822858462356, 0.05854480828158965, 0.03224116968492821, 0.00314842516193097, 0.07419711165049397, 0.02359647276941201, -0.038315040232391524, -0.13008219645744937, 0.04809569468799299, 0.11358035110383793, -0.0008055347480333437, 0.005091573107340819, 0.060200029664292026, -0.0024571384021390454, -0.055526666769903844, 0.04311087585933607, -0.012910185874900955, 0.03641633986991859, -0.01073932830906181, -0.035683445843721434, 0.07111365622285304, 0.008892221914576495, -0.03595879890625129, -0.02189642234590456, 0.03437962924602866, 0.07523445510493322, 0.024604139023921556, -0.07536518053015706, 0.0013732027183571485, 0.013400048103379927, -0.06962923942604046, -0.11895692248648887, 0.03515621860049381, 0.030757003636965236, -0.08321385364219519, -0.07156324294639715, -0.025557876422591642, -0.03765632412780067, -0.13149137498248004, -0.05013333949990793, -0.004280960985414056, -0.08930633188859516, -0.11155207776591296, -0.11272716266107619, -0.039037029472329884, -0.06029796194261389, -0.001158120617947192, -0.05575023052616491, -0.015168309620954792, -0.09349512506780935, -0.03861450989300231, -0.05444519331014207, -0.0035390067064221473, -0.059304853959784604, -0.09547908359243854, 0.1252451211859959, -0.047724855480329634, -0.11447552297963215, -0.03797424606473438, 0.04970848198959784, 0.005605197045371393, -0.005624602872811739])

def label_breathing_pattern(heights, prominence_threshold):

    # Find peaks (inhales)

    peaks, _ = find_peaks(heights, distance=10, prominence=2.2)

 

    # Find minima (exhales)

    minima, _ = find_peaks(-heights, distance=10, prominence=prominence_threshold)

 

    # Combine peaks and minima indices

    events = np.sort(np.concatenate([peaks, minima]))

 

    # Create a label array

    labels = np.zeros_like(heights, dtype=int)

 

    # Assign labels to inhales (1) and exhales (-1)

    labels[events] = np.where(np.isin(events, peaks), 1, -1)

 

    return labels, peaks, minima

# Example usage:

# Your array of points representing stomach compression heights

prominence_threshold = 2.2  # Adjust this threshold as needed
time_per_sample = 0.0525

 

breathing_labels, inhale_peaks, _ = label_breathing_pattern(data, prominence_threshold)

 

# Calculate breathing rate

rate = calculate_breathing_rate(inhale_peaks, time_per_sample)

 

print(f"Breathing Rate: {rate:.2f} breaths per minute")

 

# Plot the heights with peaks and minima highlighted

import numpy as np

import matplotlib.pyplot as plt

from scipy.signal import find_peaks

 
time_ratio = 18.8
 

# Example usage:

prominence_threshold = 0.8  # Adjust this threshold as needed

 

breathing_labels, exhale_minima, inhale_peaks = label_breathing_pattern(data, prominence_threshold)

inhale_peaks_c=inhale_peaks

exhale_minima_c=exhale_minima

# Plot the heights with peaks and minima highlighted

'''

for i in range(0, len(exhale_minima), 2):

    plt.axvspan(inhale_peaks[i], exhale_minima[i], color='red', alpha=0.3, label='Exhale Region')

'''
print(inhale_peaks_c)
print(exhale_minima_c)

show(inhales, exhales)

