## Rangsiman Ketkaew
## 27-Dec-2017
## Compute total energy of molecule at different electronics state/structures
## electron reorganization energy

for NUM in {1..10}
do
cd /f00/ccu/nutt/Complex-Ru-BL-${NUM}-Re/Truncated-Model-Acc-BL${NUM}
  dir=`pwd`
  echo "== $dir"
  E1=`grep 'SCF D' *ECP_Neu.log | awk '{print $5}'|tail -1|sed -n '1p'`
  E2=`grep 'SCF D' *ECP_An.log | awk '{print $5}'|tail -1|sed -n '1p'`
  E3=`grep 'SCF D' *ECP_Neu_SP_An.log | awk '{print $5}'|tail -1|sed -n '1p'`
  E4=`grep 'SCF D' *ECP_An_SP_Neu.log | awk '{print $5}'|tail -1|sed -n '1p'`
#  echo "E_Neu_S_Neu       = " $E1
#  echo "E_Charge_S_Charge = " $E2
#  echo "E_Charge_S_Neu    = " $E3
#  echo "E_Neu_S_Charge    = " $E4
  Free_E_hartree=`echo $E1 - $E2|bc`; Free_E_eV=`expr $Free_E_hartree*27.2116|bc`
  Reor_E_hartree=`echo $E4 - $E1 + $E3 - $E2|bc`; Reor_E_eV=`expr $Reor_E_hartree*27.2116|bc`
  echo "== Free Energy is 		     = $Free_E_hartree  hartree"
  echo "== Free Energy is 		     = $Free_E_eV  eV"
  echo "== Electron Reorganization Energy is = $Reor_E_hartree  hartree"
  echo "== Electron Reorganization Energy is = $Reor_E_eV  eV"
  echo "--------------------------------------------------------------------"
 ## echo "=========== Electron Reorganization Energy =" $(expr ($E4-$E1) + ($E3-$E2)|bc -l)
done

