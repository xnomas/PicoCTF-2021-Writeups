#============================================================================#
#============================ARCANE CALCULATOR===============================#
#============================================================================#

import hashlib
from cryptography.fernet import Fernet
import base64



# GLOBALS --v
arcane_loop_trial = True
jump_into_full = False
full_version_code = ""

username_trial = "FREEMAN"
bUsername_trial = b"FREEMAN"

key_part_static1_trial = "picoCTF{1n_7h3_|<3y_of_"
key_part_dynamic1_trial = "xxxxxxxx"
key_part_static2_trial = "}"
key_full_template_trial = key_part_static1_trial + key_part_dynamic1_trial + key_part_static2_trial

star_db_trial = {
  "Alpha Centauri": 4.38,
  "Barnard's Star": 5.95,
  "Luhman 16": 6.57,
  "WISE 0855-0714": 7.17,
  "Wolf 359": 7.78,
  "Lalande 21185": 8.29,
  "UV Ceti": 8.58,
  "Sirius": 8.59,
  "Ross 154": 9.69,
  "Yin Sector CL-Y d127": 9.86,
  "Duamta": 9.88,
  "Ross 248": 10.37,
  "WISE 1506+7027": 10.52,
  "Epsilon Eridani": 10.52,
  "Lacaille 9352": 10.69,
  "Ross 128": 10.94,
  "EZ Aquarii": 11.10,
  "61 Cygni": 11.37,
  "Procyon": 11.41,
  "Struve 2398": 11.64,
  "Groombridge 34": 11.73,
  "Epsilon Indi": 11.80,
  "SPF-LF 1": 11.82,
  "Tau Ceti": 11.94,
  "YZ Ceti": 12.07,
  "WISE 0350-5658": 12.09,
  "Luyten's Star": 12.39,
  "Teegarden's Star": 12.43,
  "Kapteyn's Star": 12.76,
  "Talta": 12.83,
  "Lacaille 8760": 12.88
}


def intro_trial():
    print("\n===============================================\n\
Welcome to the Arcane Calculator, " + username_trial + "!\n")    
    print("This is the trial version of Arcane Calculator.")
    print("The full version may be purchased in person near\n\
the galactic center of the Milky Way galaxy. \n\
Available while supplies last!\n\
=====================================================\n\n")


def menu_trial():
    print("___Arcane Calculator___\n\n\
Menu:\n\
(a) Estimate Astral Projection Mana Burn\n\
(b) [LOCKED] Estimate Astral Slingshot Approach Vector\n\
(c) Enter License Key\n\
(d) Exit Arcane Calculator")

    choice = input("What would you like to do, "+ username_trial +" (a/b/c/d)? ")
    
    if not validate_choice(choice):
        print("\n\nInvalid choice!\n\n")
        return
    
    if choice == "a":
        estimate_burn()
    elif choice == "b":
        locked_estimate_vector()
    elif choice == "c":
        enter_license()
    elif choice == "d":
        global arcane_loop_trial
        arcane_loop_trial = False
        print("Bye!")
    else:
        print("That choice is not valid. Please enter a single, valid \
lowercase letter choice (a/b/c/d).")


def validate_choice(menu_choice):
    if menu_choice == "a" or \
       menu_choice == "b" or \
       menu_choice == "c" or \
       menu_choice == "d":
        return True
    else:
        return False


def estimate_burn():
  print("\n\nSOL is detected as your nearest star.")
  target_system = input("To which system do you want to travel? ")

  if target_system in star_db_trial:
      ly = star_db_trial[target_system]
      mana_cost_low = ly**2
      mana_cost_high = ly**3
      print("\n"+ target_system +" will cost between "+ str(mana_cost_low) \
+" and "+ str(mana_cost_high) +" stone(s) to project to\n\n")
  else:
      # TODO : could add option to list known stars
      print("\nStar not found.\n\n")


def locked_estimate_vector():
    print("\n\nYou must buy the full version of this software to use this \
feature!\n\n")


def enter_license():
    user_key = input("\nEnter your license key: ")
    user_key = user_key.strip()

    global bUsername_trial
    
    if check_key(user_key, bUsername_trial):
        decrypt_full_version(user_key)
    else:
        print("\nKey is NOT VALID. Check your data entry.\n\n")


def check_key(key, username_trial):

    global key_full_template_trial

    if len(key) != len(key_full_template_trial):
        return False
    else:
        # Check static base key part --v
        i = 0
        for c in key_part_static1_trial:
            if key[i] != c:
                return False

            i += 1

        # TODO : test performance on toolbox container
        # Check dynamic part --v
        if key[i] != hashlib.sha256(username_trial).hexdigest()[4]:
            return False
        else:
            i += 1

        if key[i] != hashlib.sha256(username_trial).hexdigest()[5]:
            return False
        else:
            i += 1

        if key[i] != hashlib.sha256(username_trial).hexdigest()[3]:
            return False
        else:
            i += 1

        if key[i] != hashlib.sha256(username_trial).hexdigest()[6]:
            return False
        else:
            i += 1

        if key[i] != hashlib.sha256(username_trial).hexdigest()[2]:
            return False
        else:
            i += 1

        if key[i] != hashlib.sha256(username_trial).hexdigest()[7]:
            return False
        else:
            i += 1

        if key[i] != hashlib.sha256(username_trial).hexdigest()[1]:
            return False
        else:
            i += 1

        if key[i] != hashlib.sha256(username_trial).hexdigest()[8]:
            return False



        return True


def decrypt_full_version(key_str):

    key_base64 = base64.b64encode(key_str.encode())
    f = Fernet(key_base64)

    try:
        with open("keygenme.py", "w") as fout:
          global full_version
          global full_version_code
          full_version_code = f.decrypt(full_version)
          fout.write(full_version_code.decode())
          global arcane_loop_trial
          arcane_loop_trial = False
          global jump_into_full
          jump_into_full = True
          print("\nFull version written to 'keygenme.py'.\n\n"+ \
                 "Exiting trial version...")
    except FileExistsError:
    	sys.stderr.write("Full version of keygenme NOT written to disk, "+ \
	                  "ERROR: 'keygenme.py' file already exists.\n\n"+ \
			  "ADVICE: If this existing file is not valid, "+ \
			  "you may try deleting it and entering the "+ \
			  "license key again. Good luck")

def ui_flow():
    intro_trial()
    while arcane_loop_trial:
        menu_trial()



# Encrypted blob of full version
full_version = \
b"""
gAAAAABgT_nvdPbQsvAhvsNvjCeuMqNP4gGInWyNCirwqXlGMM4EDHMeVEIci77G1dQTtGCgsVSeUfJKzwcBldLozZ24_kcrd9fd-a81-z2KBOrI8Qv_IOhY1LqsooySaeEQMvjMqBhhLhoIDfsXBSWnEb8RPDXVzZhc_5WaNDorzw8lUMqf1vLI8bWCP97UnQZclfIa_hH-ib5hy6hXuimvny4X9-eOzEIAROHD5l-FB8r82ZfUiPKED2woAgROd1_PF9HrCN_Poi_b5D42E_-R4fTX5G6ASWexix3vtO9jXW9YqSI4mN-RMoTLcYHe6wAt89e-SnhmmVxdqXzsbx37Z0UNaEEToIaUqEWuI5hHWRx9ytb9GQLimBzBVd3ZS1vuOp4gYaxRzCy8tAR63G3QrEx3mo-XLPRm8ajHVMxlsbc5U9D11znoZKEYZd2zTjTPGxaHwXaQA7hw4ZWHEEQIAUaBtAJtB_Ua0ERrop1xG1P6U-zlAWKzzymqYIV88_yHqChyWta8291J-QTy5sYYsbWygg65G5Ea4G30Eu5I6izqanJMhMFTLcBSKx_b0HBokRvim65ywa8tCh4iYZFHDsOqr2kDgyq2pZuvSRRTEHaPJVct68QScVLmWlBXSIM36ng4izANXH1qWTMxakfHQ52MRKmKhRV3sVUHGgHqdtQWJPnIeKlnWw6bHUtGxAvCQLTgwO6HR3D5EAiHMB6qu5yiAxRJMWophLMIZNN0alYV2VX0Amvd54WqAW9MnO0q1sunAyao7l1JJe6bGYIeKSYwyRiQVKtQ2nOkWXuJCRPY3PsfcT9OAkfKRCowlGF_hPmgCpB3izpUNOAD8HuNrkqKIUhROAOU-WCa04rQ2ig7bETXfJJldPRQGCvHC9zzczQC-ppq1G5PWs_tjT8VwtrrOc_Nb14dGqbLkDuKdPMa09TJKhBto0kD8O0f-JO--TOl51bPSitqTT11E1ZLiRufSojQDDbpFBMTFJNzf5puj4r3JJnDERw0quqGU8IxBPR91ZfKKEjW1U44p5G5GBbHVN1JTb0j4hpQAyKbWQKs7kGIyuToTL0VKR0WBovSeOwR_O4KmDit6ncHHEBXt7FBD6BCWkmUPuiF2QfIIFW83AizJfilZ4YhIOjiBW2J3b7-CJj0Vayq8eZY_ZeDiehwErGeiuxgeH96TZVA3C9-vAnNjdSJLPGLU935tuv74HOsPln5zQCiNyhJ3JZR4BaWLyex3haa1X-XJJZLgeGAVNqtU0ByUR5nLG37tKF9POPEkTH7Z7ujMVtcH9GfK231Fm9giBurP2CQmInoyp_oyuErlBFDPH0p5F8qWx1zcgOUZBTscZPtCzrT4otRh0HCNSV0blYPwxPjvpW2Nqs-ojXjjRgMOS6prdbtTm0eiCMC0DLY9b4YY7Gt5CKYX4HM8eyaY8Z04WPCpVvqEOLTl4NSqUlWRaVEUcbCBQNdyHIFeUbDUrs9PjXa4_WMwbqMnBPzQmBzmx4KqJJZz9RCy7I0BeqP_wy0kcTV5q8SPfZPyz_WoHx65e3z0GCuxZrzN1D7rj_WLsTPp96oCkF3B9yBx81UKXgZodZrUGooEJLxglMTCwX35X_GTh2aIggPah_k8emL1_rX_psDqGlDUPMYj8Af_O1KinL9lylCtHgGYLyGInBzHMgv4ixHPqqHk56YFmsKgqWUwR8g9an8eevQwm9_KAcg6VzreQEYsCjnsGLKvEMHt7ll3QfwhHiW-GHnPWxvhk169hKVaidBXuJuHmOpsQad5eJyvywwg0Hx0cfd6cKi3RS4PQcaYBlQXw7nsQ3xDLk0s6Bv97G3MAyQ_FIi5ieHdWO1FMYW1kbZy3Zrx5muiRmoNEBaTyDVeko8rJ9aaZWEXV1gQdDVAr92bFT_tb2ZImbPc2yJxmynaRV40ZCnVuxmwLVwCq36BSLss6yz_vnUVpswWQ4qKDbFbdPAof9mkNt0fe4Vqe_MC4ZhVvWSlsJhTlMvLedsrTbp3mL2JGvBOfvxwiOGkO-XgW1F7TGMXzh8j-KbTVKHdt6xp3DRs1Uhae5hncMCaIGqq5ocTO9Id-esyaJEumEL7oR-uzYXss3z6rSOjnGDF0k0aWCCFEKMWe1zzYhZis74IsFZ7cCfV0daXkrdD7VFIgor0ifd4-DoLYxIr-eC-yLc7eVouoHHirk0PcrMC2w7SuXReCuYvMt-jcUlZBEphb9D_0IEZDsua_Rl62FwT-1wPzyZg_uGcUviq1h8Bkgh0rs4DBdheLwRg3k6ekdTzPA78bqk5qnSbSyJMD5fK4daKbplPcNFLHTMJzKSAhQeGx0Uw3NS70q_k2uLXvbaagMB5NHzM7ZzH8P5chxcT07hkNNt7dfu9_ux35z6sEIeCmQ-MqvVn4GRBK3zEF2t_PYsQw_da6lbzEiPVWIlqQUkFcmyhsL9hSFDeBkK18abEknjs3cdukrD-e9JRKdxRJxJW97gJM-btsh_5Nbf1pIz-uxQbQhBZQkHOqC4BWyLjg3xT92B-3yDmZnykvk7d8pXNHOwtXSHtBD0jCAdCzUyE9_U51p7icO8toV0sbZ9tj22tPe1DKMM5M2uMHQXCySv4oTGpTGp4xA4tD5Wo_o59zgzwlpXtKukU7cT8DS2NCBRlDW_2L6HojArs2NPeKtBm_-DIDCiSrHSYdiITZq7GaoeyAywiOiqlVNDdLy0p3lcNW_Yo4vXyzfSm8qXTfEpoAb9gPps0LbJhci1sWqNL9JJPI4yIca4r0rr9Y1wIEYuwXeyLoQD_Yn6xPRiVmuGSnco3HsIBOuDoyU3AGQOczn_QZ_TvyIJYdS8op8UJFRMD7W7lJWFe-ivoFdUlAjMqyDCUO_PbAeJYaE0ekh7xh3yudd7dMmD9LcTOi_LQoEfYjPXIEQPaC7D_SDYw8AbBJ51FyKSif7n_fW6_PU0U6vfYZwbPWU5tp0nNjTuaPxI_88tyuZC_2gW3YgAIWs4vo0zWBk9AvdgfxNwFiIdp4dugGGg0-dJp_SW_XzgGv1ALkaMbxiOYSK0sE8ZXb3_5zA3vUn2OsKpCq6ROt4poLIFce_Cot1RSU3FUYie2V4GT7ChUrq-vJfTPVlixee1gSPE7TnlyAm_kANyQ3_VFgIyEiEfGBLb_mlIWbVCO9e9QC6_SDKbc8UvuXodJ9HcDe-yWTjV7V-7s7-Qhp_WSIBVwex8tmyCo5W69An5eOrPRwK5NfCFp0uJClvim9qfLnVDXc5QQmajx61VuwnCVZg82iWxMh_Jms-2EiaCEz1oyB87F_awJ413I_kT8Wa6OW1ZhadZkDS5IVEZTNYwIxeIaVUoZLSBESHwwwzD7zsR02pGlJFJcWcvdI96wtCcx1os6g_Lq7tpTwd33zCA-RgYZWTHKPnFSi1z0h-RsyCIqbBmGx2eswpfJbKRKi_QFQMw60w7O41FWQL8ZluxBOSd3kSP5xyVJC7bnDfE3g_OnBdU5MFQGl6uFaIxr1lUt98GeD6Gt2X1A-Hi1zOF4iaxCbb9h9FECqUrwGlwGo_TY_W0ekFM1UXFVVcUwsCwm5hL_wC7hCcN5Ad4dWx9EAL4NX3_N8n9qC3hW_l34Cq5V4Xzm1O7T7py7XF_CZ_Xd_GDdU89f2hrV1IngHqey_fc9lTroIhoLeZ3v2nj7_9osKs7qLHa_QwnwQ5jH0LxhAOGS9FHLBGdn3tXnRyzglLLOTP3XR1qeoSOEqz4Uk13qfI3GRiHacUnyyyT2OHdi4IsrxlxzGNEjBMDws9FPjXH4Xv_R0iSeD77JBIKqgd0n0hxaZRu8lOUhmnJFHpe6OrnmK8nB4A-yHuI5z37zC3KJDgKxnBBs8zfAOP0-g==
"""



# Enter main loop
ui_flow()

if jump_into_full:
    exec(full_version_code)
