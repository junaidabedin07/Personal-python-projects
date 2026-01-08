# **Problem Statement:**
#  Implement a sliding window generator that extracts fixed-size overlapping segments from a sequence of sensor data while discarding incomplete windows.

#  **Use in IoT:**
#  Sliding windows are used to convert continuous sensor streams into fixed-size inputs required by ML and signal processing algorithms.
#  This technique enables real-time analysis of vibration, audio, ECG, and motion data on resource-constrained IoT devices.

def slider(array,a):
    i = 0
    l = len(array)
    for n in range(l):# "while True" is also correct
        if len(array[i:i+a]) < a :
            break
        yield array[i:i+a]
        i += 1
L = [1,2,3,4,5,6,7,8,9,10,11,12,13]
print(list(slider(L,3)))

#use json or CSVs for better understanding of both the topics