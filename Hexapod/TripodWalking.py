import math
import numpy as np
import pybullet as p
import pybullet_data
from time import sleep

while(1):
    fpos = [[511.35786630447177, 591.5780892521681, 462.3266396024213, 514.9225497648482, 587.4530031551449, 468.04056543550837, 511.35786630447177, 591.5780892521681, 462.3266396024213, 514.9225497648482, 587.4530031551449, 468.04056543550837, 511.35786630447177, 591.5780892521681, 462.3266396024213, 514.9225497648482, 587.4530031551449, 468.04056543550837], [507.322474382833, 612.5924475935865, 444.52962987077944, 520.4922793305251, 586.2667114510112, 473.32021190099135, 507.322474382833, 612.5924475935865, 444.52962987077944, 520.4922793305251, 586.2667114510112, 473.32021190099135, 507.322474382833, 612.5924475935865, 444.52962987077944, 520.4922793305251, 586.2667114510112, 473.32021190099135], [500.48132568664073, 642.34497811306, 421.09251504599587, 527.7312945607965, 584.3395115943908, 481.0686129659561, 500.48132568664073, 642.34497811306, 421.09251504599587, 527.7312945607965, 584.3395115943908, 481.0686129659561, 500.48132568664073, 642.34497811306, 421.09251504599587, 527.7312945607965, 584.3395115943908, 481.0686129659561], [491.40234839897687, 670.6774277598871, 399.9890598302383, 535.7142418011038, 581.592500557568, 490.96668955200005, 491.40234839897687, 670.6774277598871, 399.9890598302383, 535.7142418011038, 581.592500557568, 490.96668955200005, 491.40234839897687, 670.6774277598871, 399.9890598302383, 535.7142418011038, 581.592500557568, 490.96668955200005], [480.7409969893733, 687.7019315020871, 386.14703091592816, 543.6453985744755, 578.0463825884942, 502.4885693741388, 480.7409969893733, 687.7019315020871, 386.14703091592816, 543.6453985744755, 578.0463825884942, 502.4885693741388, 480.7409969893733, 687.7019315020871, 386.14703091592816, 543.6453985744755, 578.0463825884942, 502.4885693741388], [469.30738039141283, 686.6736957700475, 382.01852703488237, 550.8907885622883, 573.8993082385005, 514.8093820187698, 469.30738039141283, 686.6736957700475, 382.01852703488237, 550.8907885622883, 573.8993082385005, 514.8093820187698, 469.30738039141283, 686.6736957700475, 382.01852703488237, 550.8907885622883, 573.8993082385005, 514.8093820187698], [458.0798629969671, 667.4068976572662, 388.34497019741644, 556.9672496288911, 569.5763424966327, 526.7582309251303, 458.0798629969671, 667.4068976572662, 388.34497019741644, 556.9672496288911, 569.5763424966327, 526.7582309251303, 458.0798629969671, 667.4068976572662, 388.34497019741644, 556.9672496288911, 569.5763424966327, 526.7582309251303], [448.1632094212198, 637.4129489581077, 403.22623418599505, 561.4994273607418, 565.7328673052327, 536.8258800171858, 448.1632094212198, 637.4129489581077, 403.22623418599505, 561.4994273607418, 565.7328673052327, 536.8258800171858, 448.1632094212198, 637.4129489581077, 403.22623418599505, 561.4994273607418, 565.7328673052327, 536.8258800171858], [440.71374789055983, 608.4670398213395, 420.81514153555503, 564.1571240677902, 563.1884485472707, 543.2632858978745, 440.71374789055983, 608.4670398213395, 420.81514153555503, 564.1571240677902, 563.1884485472707, 543.2632858978745, 440.71374789055983, 608.4670398213395, 420.81514153555503, 564.1571240677902, 563.1884485472707, 543.2632858978745], [436.86941581304643, 591.7750334378447, 432.2609314790636, 564.579075626252, 562.7626386285319, 544.3251043491948, 436.86941581304643, 591.7750334378447, 432.2609314790636, 564.579075626252, 562.7626386285319, 544.3251043491948, 436.86941581304643, 591.7750334378447, 432.2609314790636, 564.579075626252, 562.7626386285319, 544.3251043491948]]
    fvel = [[28.8975623069927, 137.34320949897995, 120.69142554811859, 48.09178306833259, 13.301196459284467, 43.750618671739204, 28.8975623069927, 137.34320949897995, 120.69142554811859, 48.09178306833259, 13.301196459284467, 43.750618671739204, 28.8975623069927, 137.34320949897995, 120.69142554811859, 48.09178306833259, 13.301196459284467, 43.750618671739204], [59.061030156394516, 268.98743133973693, 221.61579200775665, 69.18619227791402, 20.050984233774518, 69.08746179520135, 59.061030156394516, 268.98743133973693, 221.61579200775665, 69.18619227791402, 20.050984233774518, 69.08746179520135, 59.061030156394516, 268.98743133973693, 221.61579200775665, 69.18619227791402, 20.050984233774518, 69.08746179520135], [83.77817782349118, 305.9120970740741, 233.30329536858727, 80.81868571031463, 27.769832746208685, 91.89940590838246, 83.77817782349118, 305.9120970740741, 233.30329536858727, 80.81868571031463, 27.769832746208685, 91.89940590838246, 83.77817782349118, 305.9120970740741, 233.30329536858727, 80.81868571031463, 27.769832746208685, 91.89940590838246], [102.66239737825177, 241.39881649324226, 181.39838762165584, 83.94909084949273, 35.91454504853647, 110.76952485913553, 102.66239737825177, 241.39881649324226, 181.39838762165584, 83.94909084949273, 35.91454504853647, 110.76952485913553, 102.66239737825177, 241.39881649324226, 181.39838762165584, 83.94909084949273, 35.91454504853647, 110.76952485913553], [114.45317219984439, 89.82358324055703, 95.41189165251156, 80.07693948500008, 43.09888738286914, 123.1511062382964, 114.45317219984439, 89.82358324055703, 95.41189165251156, 80.07693948500008, 43.09888738286914, 123.1511062382964, 114.45317219984439, 89.82358324055703, 95.41189165251156, 80.07693948500008, 43.09888738286914, 123.1511062382964], [117.47662177276673, 110.50711653286655, 16.10004659997493, 70.7930769132075, 47.28639918860689, 125.81696766426151, 117.47662177276673, 110.50711653286655, 16.10004659997493, 70.7930769132075, 47.28639918860689, 125.81696766426151, 117.47662177276673, 110.50711653286655, 16.10004659997493, 70.7930769132075, 47.28639918860689, 125.81696766426151], [110.21209313051432, 263.26607491971157, 114.78321812196982, 57.4026538584214, 46.151329266114615, 115.31372825641505, 110.21209313051432, 263.26607491971157, 114.78321812196982, 57.4026538584214, 46.151329266114615, 115.31372825641505, 110.21209313051432, 263.26607491971157, 114.78321812196982, 57.4026538584214, 46.151329266114615, 115.31372825641505], [91.76593998530817, 313.0214879414932, 176.4741859076763, 40.67733178060662, 37.62824339852239, 88.62374396290888, 91.76593998530817, 313.0214879414932, 176.4741859076763, 40.67733178060662, 37.62824339852239, 88.62374396290888, 91.76593998530817, 313.0214879414932, 176.4741859076763, 40.67733178060662, 37.62824339852239, 88.62374396290888], [62.01321498980011, 244.31413874130772, 162.33093164731946, 20.707964780527135, 20.736084558539957, 44.31848801687362, 62.01321498980011, 244.31413874130772, 162.33093164731946, 20.707964780527135, 20.736084558539957, 44.31848801687362, 62.01321498980011, 244.31413874130772, 162.33093164731946, 20.707964780527135, 20.736084558539957, 44.31848801687362], [21.38593835089286, 78.43780394507291, 57.432652980791154, 13.231271398998254, 13.367428261205294, 25.8240705842148, 21.38593835089286, 78.43780394507291, 57.432652980791154, 13.231271398998254, 13.367428261205294, 25.8240705842148, 21.38593835089286, 78.43780394507291, 57.432652980791154, 13.231271398998254, 13.367428261205294, 25.8240705842148]]
    lpos = [[440.71374789055983, 591.7731363294365, 432.88540622504405, 564.1571240677902, 566.3373005101238, 540.7000367966732, 440.71374789055983, 591.7731363294365, 432.88540622504405, 564.1571240677902, 566.3373005101238, 540.7000367966732, 440.71374789055983, 591.7731363294365, 432.88540622504405, 564.1571240677902, 566.3373005101238, 540.7000367966732], [448.1632094212198, 591.755548662114, 434.35213881390894, 561.4994273607418, 586.908460007666, 520.4007706258227, 448.1632094212198, 591.755548662114, 434.35213881390894, 561.4994273607418, 586.908460007666, 520.4007706258227, 448.1632094212198, 591.755548662114, 434.35213881390894, 561.4994273607418, 586.908460007666, 520.4007706258227], [458.07986299696717, 591.6843782321881, 436.86162804659796, 556.9672496288911, 615.2765943469665, 493.661270967032, 458.07986299696717, 591.6843782321881, 436.86162804659796, 556.9672496288911, 615.2765943469665, 493.661270967032, 458.07986299696717, 591.6843782321881, 436.86162804659796, 556.9672496288911, 615.2765943469665, 493.661270967032], [469.30738039141283, 591.4916807905948, 440.5464511741252, 550.8907885622883, 642.154207202533, 468.5647718568622, 469.30738039141283, 591.4916807905948, 440.5464511741252, 550.8907885622883, 642.154207202533, 468.5647718568622, 469.30738039141283, 591.4916807905948, 440.5464511741252, 550.8907885622883, 642.154207202533, 468.5647718568622], [480.7409969893733, 591.0966711875006, 445.3443806262417, 543.6453985744755, 659.7937155872382, 449.4720734409459, 480.7409969893733, 591.0966711875006, 445.3443806262417, 543.6453985744755, 659.7937155872382, 449.4720734409459, 480.7409969893733, 591.0966711875006, 445.3443806262417, 543.6453985744755, 659.7937155872382, 449.4720734409459], [491.4023483989769, 590.4531662116735, 450.92253611339635, 535.7142418011038, 663.0066543658461, 438.55810402310334, 491.4023483989769, 590.4531662116735, 450.92253611339635, 535.7142418011038, 663.0066543658461, 438.55810402310334, 491.4023483989769, 590.4531662116735, 450.92253611339635, 535.7142418011038, 663.0066543658461, 438.55810402310334], [500.48132568664073, 589.6077140710967, 456.6561983735094, 527.7312945607965, 650.6906014768025, 437.11380358992375, 500.48132568664073, 589.6077140710967, 456.6561983735094, 527.7312945607965, 650.6906014768025, 437.11380358992375, 500.48132568664073, 589.6077140710967, 456.6561983735094, 527.7312945607965, 650.6906014768025, 437.11380358992375], [507.322474382833, 588.7317445133933, 461.6687816144609, 520.4922793305251, 627.436136597347, 444.623716558918, 507.322474382833, 588.7317445133933, 461.6687816144609, 520.4922793305251, 627.436136597347, 444.623716558918, 507.322474382833, 588.7317445133933, 461.6687816144609, 520.4922793305251, 627.436136597347, 444.623716558918], [511.35786630447177, 588.0973095310935, 464.9394208548222, 514.9225497648482, 602.8589997961882, 456.73630346347807, 511.35786630447177, 588.0973095310935, 464.9394208548222, 514.9225497648482, 602.8589997961882, 456.73630346347807, 511.35786630447177, 588.0973095310935, 464.9394208548222, 514.9225497648482, 602.8589997961882, 456.73630346347807], [512.0, 587.987327635526, 465.482924046675, 512.0, 587.987327635526, 465.482924046675, 512.0, 587.987327635526, 465.482924046675, 512.0, 587.987327635526, 465.482924046675, 512.0, 587.987327635526, 465.482924046675, 512.0, 587.987327635526, 465.482924046675]]
    lvel = [[62.01321498979725, 5.056982485606142, 14.917669231324467, 20.70796478052717, 136.399235467411, 137.69205361216035, 62.01321498979725, 5.056982485606142, 14.917669231324467, 20.70796478052717, 136.399235467411, 137.69205361216035, 62.01321498979725, 5.056982485606142, 14.917669231324467, 20.70796478052717, 136.399235467411, 137.69205361216035], [91.76593998530745, 5.347061693687269, 24.11318629475999, 40.67733178060665, 260.0836876816656, 251.20707081298664, 91.76593998530745, 5.347061693687269, 24.11318629475999, 40.67733178060665, 260.0836876816656, 251.20707081298664, 91.76593998530745, 5.347061693687269, 24.11318629475999, 40.67733178060665, 260.0836876816656, 251.20707081298664], [110.21209313051435, 6.157609125569116, 35.18481219972479, 57.40265385842139, 289.1956254866755, 268.23183477967865, 110.21209313051435, 6.157609125569116, 35.18481219972479, 57.40265385842139, 289.1956254866755, 268.23183477967865, 110.21209313051435, 6.157609125569116, 35.18481219972479, 57.40265385842139, 289.1956254866755, 268.23183477967865], [117.47662177276655, 7.749536651826661, 46.765812920124446, 70.79307691320751, 233.50249666127485, 225.63507512951435, 117.47662177276655, 7.749536651826661, 46.765812920124446, 70.79307691320751, 233.50249666127485, 225.63507512951435, 117.47662177276655, 7.749536651826661, 46.765812920124446, 70.79307691320751, 233.50249666127485, 225.63507512951435], [114.45317219984439, 10.058714412825482, 56.49663944750451, 80.07693948500007, 112.65431655500664, 154.36060719884847, 114.45317219984439, 10.058714412825482, 56.49663944750451, 80.07693948500007, 112.65431655500664, 154.36060719884847, 114.45317219984439, 10.058714412825482, 56.49663944750451, 80.07693948500007, 112.65431655500664, 154.36060719884847], [102.6623973782519, 12.452197970618638, 61.53405868952669, 83.94909084949273, 51.97175539368452, 66.73067709491845, 102.6623973782519, 12.452197970618638, 61.53405868952669, 83.94909084949273, 51.97175539368452, 66.73067709491845, 102.6623973782519, 12.452197970618638, 61.53405868952669, 83.94909084949273, 51.97175539368452, 66.73067709491845], [83.7781778234913, 13.793646185060148, 59.11546842478154, 80.81868571031463, 191.2590387837976, 38.088167750460485, 83.7781778234913, 13.793646185060148, 59.11546842478154, 80.81868571031463, 191.2590387837976, 38.088167750460485, 83.7781778234913, 13.793646185060148, 59.11546842478154, 80.81868571031463, 191.2590387837976, 38.088167750460485], [59.06103015639439, 12.873660320530487, 47.18974992396773, 69.18619227791383, 257.01151827109857, 111.64567404126888, 59.06103015639439, 12.873660320530487, 47.18974992396773, 69.18619227791383, 257.01151827109857, 111.64567404126888, 59.06103015639439, 12.873660320530487, 47.18974992396773, 69.18619227791383, 257.01151827109857, 111.64567404126888], [28.897562306992693, 9.045081857588155, 25.106071801812526, 48.09178306833267, 214.87862123461787, 121.47516724545102, 28.897562306992693, 9.045081857588155, 25.106071801812526, 48.09178306833267, 214.87862123461787, 121.47516724545102, 28.897562306992693, 9.045081857588155, 25.106071801812526, 48.09178306833267, 214.87862123461787, 121.47516724545102], [17.530202168677096, 7.171442707744457, 15.669226338508931, 17.53020216867712, 71.40446059378033, 46.19131687652185, 17.530202168677096, 7.171442707744457, 15.669226338508931, 17.53020216867712, 71.40446059378033, 46.19131687652185, 17.530202168677096, 7.171442707744457, 15.669226338508931, 17.53020216867712, 71.40446059378033, 46.19131687652185]]
    pos = [[443.04216735968265, 591.769951127771, 433.30691861832827, 562.9657942763092, 570.288742325424, 535.545448925694, 443.04216735968265, 591.769951127771, 433.30691861832827, 562.9657942763092, 570.288742325424, 535.545448925694, 443.04216735968265, 591.769951127771, 433.30691861832827, 562.9657942763092, 570.288742325424, 535.545448925694], [456.631377072264, 591.6993812105231, 436.4534280754719, 556.876349083665, 595.314247148193, 507.10967293601743, 456.631377072264, 591.6993812105231, 436.4534280754719, 556.876349083665, 595.314247148193, 507.10967293601743, 456.631377072264, 591.6993812105231, 436.4534280754719, 556.876349083665, 595.314247148193, 507.10967293601743], [475.0060829008834, 591.3258293670285, 442.7962424137403, 546.6782943239673, 627.8385679211584, 471.42393617603483, 475.0060829008834, 591.3258293670285, 442.7962424137403, 546.6782943239673, 627.8385679211584, 471.42393617603483, 475.0060829008834, 591.3258293670285, 442.7962424137403, 546.6782943239673, 627.8385679211584, 471.42393617603483], [495.36215342367393, 590.1235561932211, 453.30312136846726, 532.6221422506758, 658.190800540259, 437.8208966626145, 495.36215342367393, 590.1235561932211, 453.30312136846726, 532.6221422506758, 658.190800540259, 437.8208966626145, 495.36215342367393, 590.1235561932211, 453.30312136846726, 532.6221422506758, 658.190800540259, 437.8208966626145], [515.1742579814875, 587.4042946580996, 468.26744985067063, 515.1742579814875, 677.5003357267053, 412.0698292040569, 515.1742579814875, 587.4042946580996, 468.26744985067063, 515.1742579814875, 677.5003357267053, 412.0698292040569, 515.1742579814875, 587.4042946580996, 468.26744985067063, 515.1742579814875, 677.5003357267053, 412.0698292040569], [532.6221422506758, 582.7436331157973, 486.9483312836661, 495.36215342367393, 678.85417115874, 397.9801400085652, 532.6221422506758, 582.7436331157973, 486.9483312836661, 495.36215342367393, 678.85417115874, 397.9801400085652, 532.6221422506758, 582.7436331157973, 486.9483312836661, 495.36215342367393, 678.85417115874, 397.9801400085652], [546.6782943239673, 576.4287226341744, 507.41610521289493, 475.00608290088337, 661.1733501474652, 397.4983508309408, 546.6782943239673, 576.4287226341744, 507.41610521289493, 475.00608290088337, 661.1733501474652, 397.4983508309408, 546.6782943239673, 576.4287226341744, 507.41610521289493, 475.00608290088337, 661.1733501474652, 397.4983508309408], [556.876349083665, 569.6476180143903, 526.5670756233425, 456.63137707226394, 632.3122157341493, 408.47986193651656, 556.876349083665, 569.6476180143903, 526.5670756233425, 456.63137707226394, 632.3122157341493, 408.47986193651656, 556.876349083665, 569.6476180143903, 526.5670756233425, 456.63137707226394, 632.3122157341493, 408.47986193651656], [562.9657942763092, 564.3577203913848, 540.3252815665612, 443.04216735968265, 605.2737128480899, 423.4802795003583, 562.9657942763092, 564.3577203913848, 540.3252815665612, 443.04216735968265, 605.2737128480899, 423.4802795003583, 562.9657942763092, 564.3577203913848, 540.3252815665612, 443.04216735968265, 605.2737128480899, 423.4802795003583], [564.579075626252, 562.7626386285319, 544.3251043491948, 436.86941581304643, 591.7750334378447, 432.2609314790636, 564.579075626252, 562.7626386285319, 544.3251043491948, 436.86941581304643, 591.7750334378447, 432.2609314790636, 564.579075626252, 562.7626386285319, 544.3251043491948, 436.86941581304643, 591.7750334378447, 432.2609314790636], [562.9657942763092, 570.288742325424, 535.545448925694, 443.04216735968265, 591.769951127771, 433.30691861832827, 562.9657942763092, 570.288742325424, 535.545448925694, 443.04216735968265, 591.769951127771, 433.30691861832827, 562.9657942763092, 570.288742325424, 535.545448925694, 443.04216735968265, 591.769951127771, 433.30691861832827], [556.876349083665, 595.314247148193, 507.10967293601743, 456.631377072264, 591.6993812105231, 436.4534280754719, 556.876349083665, 595.314247148193, 507.10967293601743, 456.631377072264, 591.6993812105231, 436.4534280754719, 556.876349083665, 595.314247148193, 507.10967293601743, 456.631377072264, 591.6993812105231, 436.4534280754719], [546.6782943239673, 627.8385679211584, 471.42393617603483, 475.0060829008834, 591.3258293670285, 442.7962424137403, 546.6782943239673, 627.8385679211584, 471.42393617603483, 475.0060829008834, 591.3258293670285, 442.7962424137403, 546.6782943239673, 627.8385679211584, 471.42393617603483, 475.0060829008834, 591.3258293670285, 442.7962424137403], [532.6221422506758, 658.190800540259, 437.8208966626145, 495.36215342367393, 590.1235561932211, 453.30312136846726, 532.6221422506758, 658.190800540259, 437.8208966626145, 495.36215342367393, 590.1235561932211, 453.30312136846726, 532.6221422506758, 658.190800540259, 437.8208966626145, 495.36215342367393, 590.1235561932211, 453.30312136846726], [515.1742579814875, 677.5003357267053, 412.0698292040569, 515.1742579814875, 587.4042946580996, 468.26744985067063, 515.1742579814875, 677.5003357267053, 412.0698292040569, 515.1742579814875, 587.4042946580996, 468.26744985067063, 515.1742579814875, 677.5003357267053, 412.0698292040569, 515.1742579814875, 587.4042946580996, 468.26744985067063], [495.36215342367393, 678.85417115874, 397.9801400085652, 532.6221422506758, 582.7436331157973, 486.9483312836661, 495.36215342367393, 678.85417115874, 397.9801400085652, 532.6221422506758, 582.7436331157973, 486.9483312836661, 495.36215342367393, 678.85417115874, 397.9801400085652, 532.6221422506758, 582.7436331157973, 486.9483312836661], [475.00608290088337, 661.1733501474652, 397.4983508309408, 546.6782943239673, 576.4287226341744, 507.41610521289493, 475.00608290088337, 661.1733501474652, 397.4983508309408, 546.6782943239673, 576.4287226341744, 507.41610521289493, 475.00608290088337, 661.1733501474652, 397.4983508309408, 546.6782943239673, 576.4287226341744, 507.41610521289493], [456.63137707226394, 632.3122157341493, 408.47986193651656, 556.876349083665, 569.6476180143903, 526.5670756233425, 456.63137707226394, 632.3122157341493, 408.47986193651656, 556.876349083665, 569.6476180143903, 526.5670756233425, 456.63137707226394, 632.3122157341493, 408.47986193651656, 556.876349083665, 569.6476180143903, 526.5670756233425], [443.04216735968265, 605.2737128480899, 423.4802795003583, 562.9657942763092, 564.3577203913848, 540.3252815665612, 443.04216735968265, 605.2737128480899, 423.4802795003583, 562.9657942763092, 564.3577203913848, 540.3252815665612, 443.04216735968265, 605.2737128480899, 423.4802795003583, 562.9657942763092, 564.3577203913848, 540.3252815665612], [436.86941581304643, 591.7750334378447, 432.2609314790636, 564.579075626252, 562.7626386285319, 544.3251043491948, 436.86941581304643, 591.7750334378447, 432.2609314790636, 564.579075626252, 562.7626386285319, 544.3251043491948, 436.86941581304643, 591.7750334378447, 432.2609314790636, 564.579075626252, 562.7626386285319, 544.3251043491948]]
    vel = [[105.59554477114703, 5.177172989804141, 23.92661702273407, 43.498410342251006, 179.63865456273095, 207.4211898496257, 105.59554477114703, 5.177172989804141, 23.92661702273407, 43.498410342251006, 179.63865456273095, 207.4211898496257, 105.59554477114703, 5.177172989804141, 23.92661702273407, 43.498410342251006, 179.63865456273095, 207.4211898496257], [165.76578648481828, 6.5639957981445, 49.49252203536692, 85.00606613411435, 302.7272233551469, 337.08324867029705, 165.76578648481828, 6.5639957981445, 49.49252203536692, 85.00606613411435, 302.7272233551469, 337.08324867029705, 165.76578648481828, 6.5639957981445, 49.49252203536692, 85.00606613411435, 302.7272233551469, 337.08324867029705], [198.8147849153745, 11.613418505167836, 86.17729389934755, 124.01476344374002, 327.42107693507614, 355.4492115180079, 198.8147849153745, 11.613418505167836, 86.17729389934755, 124.01476344374002, 327.42107693507614, 355.4492115180079, 198.8147849153745, 11.613418505167836, 86.17729389934755, 124.01476344374002, 327.42107693507614, 355.4492115180079], [204.96055079309104, 23.090872029537792, 129.7734631422615, 160.08731484643621, 261.39186375350226, 302.4405196680285, 204.96055079309104, 23.090872029537792, 129.7734631422615, 160.08731484643621, 261.39186375350226, 302.4405196680285, 204.96055079309104, 23.090872029537792, 129.7734631422615, 160.08731484643621, 261.39186375350226, 302.4405196680285], [189.3945687028868, 40.84368177415817, 171.6010742680888, 189.39456870288683, 114.1535594774069, 204.85017306306287, 189.3945687028868, 40.84368177415817, 171.6010742680888, 189.39456870288683, 114.1535594774069, 204.85017306306287, 189.3945687028868, 40.84368177415817, 171.6010742680888, 189.39456870288683, 114.1535594774069, 204.85017306306287], [160.08731484643613, 59.836764407954476, 200.46943451790528, 204.9605507930912, 90.19532199806531, 76.96664056300757, 160.08731484643613, 59.836764407954476, 200.46943451790528, 204.9605507930912, 90.19532199806531, 76.96664056300757, 160.08731484643613, 59.836764407954476, 200.46943451790528, 204.9605507930912, 90.19532199806531, 76.96664056300757], [124.01476344374002, 71.66593110845452, 204.60038849831108, 198.81478491537456, 251.898912047256, 64.33399061742514, 124.01476344374002, 71.66593110845452, 204.60038849831108, 198.81478491537456, 251.898912047256, 64.33399061742514, 124.01476344374002, 71.66593110845452, 204.60038849831108, 198.81478491537456, 251.898912047256, 64.33399061742514], [85.00606613411435, 67.63828524721373, 173.06850454305294, 165.7657864848176, 299.8870996919735, 147.76672358389982, 85.00606613411435, 67.63828524721373, 173.06850454305294, 165.7657864848176, 299.8870996919735, 147.76672358389982, 85.00606613411435, 67.63828524721373, 173.06850454305294, 165.7657864848176, 299.8870996919735, 147.76672358389982], [43.49841034225095, 42.01655759009952, 98.54229649674397, 105.59554477114881, 219.34695553366367, 137.93958982439307, 43.49841034225095, 42.01655759009952, 98.54229649674397, 105.59554477114881, 219.34695553366367, 137.93958982439307, 43.49841034225095, 42.01655759009952, 98.54229649674397, 105.59554477114881, 219.34695553366367, 137.93958982439307], [13.231271398998254, 13.367428261205294, 25.8240705842148, 21.385938350861437, 41.71851159233246, 29.978975990242485, 13.231271398998254, 13.367428261205294, 25.8240705842148, 21.385938350861437, 41.71851159233246, 29.978975990242485, 13.231271398998254, 13.367428261205294, 25.8240705842148, 21.385938350861437, 41.71851159233246, 29.978975990242485], [43.498410342251006, 179.63865456273095, 207.4211898496257, 105.59554477114703, 5.177172989804141, 23.92661702273407, 43.498410342251006, 179.63865456273095, 207.4211898496257, 105.59554477114703, 5.177172989804141, 23.92661702273407, 43.498410342251006, 179.63865456273095, 207.4211898496257, 105.59554477114703, 5.177172989804141, 23.92661702273407], [85.00606613411435, 302.7272233551469, 337.08324867029705, 165.76578648481828, 6.5639957981445, 49.49252203536692, 85.00606613411435, 302.7272233551469, 337.08324867029705, 165.76578648481828, 6.5639957981445, 49.49252203536692, 85.00606613411435, 302.7272233551469, 337.08324867029705, 165.76578648481828, 6.5639957981445, 49.49252203536692], [124.01476344374002, 327.42107693507614, 355.4492115180079, 198.8147849153745, 11.613418505167836, 86.17729389934755, 124.01476344374002, 327.42107693507614, 355.4492115180079, 198.8147849153745, 11.613418505167836, 86.17729389934755, 124.01476344374002, 327.42107693507614, 355.4492115180079, 198.8147849153745, 11.613418505167836, 86.17729389934755], [160.08731484643621, 261.39186375350226, 302.4405196680285, 204.96055079309104, 23.090872029537792, 129.7734631422615, 160.08731484643621, 261.39186375350226, 302.4405196680285, 204.96055079309104, 23.090872029537792, 129.7734631422615, 160.08731484643621, 261.39186375350226, 302.4405196680285, 204.96055079309104, 23.090872029537792, 129.7734631422615], [189.39456870288683, 114.1535594774069, 204.85017306306287, 189.3945687028868, 40.84368177415817, 171.6010742680888, 189.39456870288683, 114.1535594774069, 204.85017306306287, 189.3945687028868, 40.84368177415817, 171.6010742680888, 189.39456870288683, 114.1535594774069, 204.85017306306287, 189.3945687028868, 40.84368177415817, 171.6010742680888], [204.9605507930912, 90.19532199806531, 76.96664056300757, 160.08731484643613, 59.836764407954476, 200.46943451790528, 204.9605507930912, 90.19532199806531, 76.96664056300757, 160.08731484643613, 59.836764407954476, 200.46943451790528, 204.9605507930912, 90.19532199806531, 76.96664056300757, 160.08731484643613, 59.836764407954476, 200.46943451790528], [198.81478491537456, 251.898912047256, 64.33399061742514, 124.01476344374002, 71.66593110845452, 204.60038849831108, 198.81478491537456, 251.898912047256, 64.33399061742514, 124.01476344374002, 71.66593110845452, 204.60038849831108, 198.81478491537456, 251.898912047256, 64.33399061742514, 124.01476344374002, 71.66593110845452, 204.60038849831108], [165.7657864848176, 299.8870996919735, 147.76672358389982, 85.00606613411435, 67.63828524721373, 173.06850454305294, 165.7657864848176, 299.8870996919735, 147.76672358389982, 85.00606613411435, 67.63828524721373, 173.06850454305294, 165.7657864848176, 299.8870996919735, 147.76672358389982, 85.00606613411435, 67.63828524721373, 173.06850454305294], [105.59554477114881, 219.34695553366367, 137.93958982439307, 43.49841034225095, 42.01655759009952, 98.54229649674397, 105.59554477114881, 219.34695553366367, 137.93958982439307, 43.49841034225095, 42.01655759009952, 98.54229649674397, 105.59554477114881, 219.34695553366367, 137.93958982439307, 43.49841034225095, 42.01655759009952, 98.54229649674397], [21.385938350861437, 41.71851159233246, 29.978975990242485, 13.231271398998254, 13.367428261205294, 25.8240705842148, 21.385938350861437, 41.71851159233246, 29.978975990242485, 13.231271398998254, 13.367428261205294, 25.8240705842148, 21.385938350861437, 41.71851159233246, 29.978975990242485, 13.231271398998254, 13.367428261205294, 25.8240705842148]]
    for i in range(0, 20):
        for j in range(0, 18):
            pos[i][j] = round(pos[i][j] / 1023 * 300 - 150, 1) * math.pi / 180
            if(vel[i][j] * 0.111 < 113.553):
                vel[i][j] = vel[i][j] * 0.111
            else:
                vel[i][j] = 113.553 - vel[i][j] * 0.111
            vel[i][j] = vel[i][j] * 2 * math.pi / 60
    break

for i in range(0, 20):
    for j in range(0, 18):
        if(j == 0):
            pos[i][j] = -pos[i][j]
        if(j == 3):
            pos[i][j] = -pos[i][j]
        if(j == 6):
            pos[i][j] = -pos[i][j]
hexaid = p.connect(p.GUI)
p.setGravity(0, 0, -9.81, physicsClientId = hexaid)
p.setAdditionalSearchPath(pybullet_data.getDataPath())
HexaPod = p.loadURDF("Hexapod.urdf", basePosition = [0, 0, 0.2])
Plane = p.loadURDF("Plane.urdf")
observation = np.zeros(63, dtype = "float32")

joint_list = [j for j in range(p.getNumJoints(HexaPod)) if p.getJointInfo(HexaPod, j)[2] == p.JOINT_REVOLUTE]
p.resetBasePositionAndOrientation(HexaPod, [0, 0, 0.2], [0, 0, 0, 1])
for j in joint_list:
    p.resetJointState(HexaPod, j, 0)
dt = 0.05
frameskip = 12
position = p.getBasePositionAndOrientation(hexaid)[0]
view_matrix = p.computeViewMatrixFromYawPitchRoll(cameraTargetPosition = position, distance = 0.6, yaw = 30, pitch = -30, roll = 0, upAxisIndex = 2)
proj_matrix = p.computeProjectionMatrixFOV(fov = 60, aspect = 960./720, nearVal = 0.1, farVal = 100.0)
px = p.getCameraImage(width = 960, height = 720, viewMatrix = view_matrix, projectionMatrix = proj_matrix, renderer = p.ER_TINY_RENDERER)[2]
p.setGravity(0, 0, -9.81, physicsClientId = hexaid)
p.stepSimulation()
p.setRealTimeSimulation(0)
for i in range(0, 10):
    for j in range(0, 18):
        p.setJointMotorControl2(bodyUniqueId = HexaPod, jointIndex = joint_list[j], controlMode = p.POSITION_CONTROL, targetPosition = fpos[i][j], force = 1.5, maxVelocity = fvel[i][j])
    for _ in range(frameskip):
        p.stepSimulation()
        sleep(dt / frameskip)
        p.setRealTimeSimulation(0)
for n in range(0, 20):
    for i in range(0, 20):
        for j in range(0, 18):
            p.setJointMotorControl2(bodyUniqueId = HexaPod, jointIndex = joint_list[j], controlMode = p.POSITION_CONTROL, targetPosition = pos[i][j], force = 1.5, maxVelocity = vel[i][j])
        for _ in range(frameskip):
            p.stepSimulation()
            sleep(dt / frameskip)
            p.setRealTimeSimulation(0)
            all_states = p.getJointStates(HexaPod, joint_list)
            for k, (posi, velo, _, torq) in enumerate(all_states):
                observation[3*k:3*k + 3] = [posi, velo, torq]
            positions = observation[0:-6:3]
            speeds = observation[1:-6:3]
            torques = observation[2:-6:3]
        #print(positions[15] * 180 / math.pi)
        #print(positions[16] * 180 / math.pi)
        #print(positions[17] * 180 / math.pi)
        #print(speeds[15] * 60 / (2 * math.pi))
        #print(speeds[16] * 60 / (2 * math.pi))
        #print(speeds[17] * 60 / (2 * math.pi))
        #print(torques[15])
        #print(torques[16])
        #print(torques[17])
for i in range(0, 10):
    for j in range(0, 18):
        p.setJointMotorControl2(bodyUniqueId = HexaPod, jointIndex = joint_list[j], controlMode = p.POSITION_CONTROL, targetPosition = lpos[i][j], force = 1.5, maxVelocity = lvel[i][j])
    for _ in range(frameskip):
        p.stepSimulation()
        sleep(dt / frameskip)
        p.setRealTimeSimulation(0)