{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 32,
   "id": "8c5e3c0b-0fe1-4128-94e6-640c18aa8e23",
   "metadata": {},
   "outputs": [],
   "source": [
    "import RPi.GPIO as gp\n",
    "import datetime\n",
    "import pandas as pd\n",
    "import numpy as np\n",
    "import matplotlib.pyplot as plt\n",
    "import csv\n",
    "import time\n",
    "import sys"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 33,
   "id": "264c77da-bde7-405f-bca7-7782abe05585",
   "metadata": {},
   "outputs": [],
   "source": [
    "cnum=0\n",
    "# Placeholder channel number"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 35,
   "id": "163db50b-4e70-440b-b341-e5ddc167cd3d",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Time Set: ['/home/pi/.local/lib/python3.9/site-packages/ipykernel_launcher.py', '-f', '/home/pi/.local/share/jupyter/runtime/kernel-8a72d6bd-5e84-4b55-89b8-9299d4a6fec8.json']\n"
     ]
    },
    {
     "ename": "ValueError",
     "evalue": "could not convert string to float: '-f'",
     "output_type": "error",
     "traceback": [
      "\u001b[0;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[0;31mValueError\u001b[0m                                Traceback (most recent call last)",
      "Cell \u001b[0;32mIn[35], line 5\u001b[0m\n\u001b[1;32m      3\u001b[0m csvwriter\u001b[38;5;241m.\u001b[39mwriterow([\u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mReal Time\u001b[39m\u001b[38;5;124m\"\u001b[39m,\u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mSeconds\u001b[39m\u001b[38;5;124m\"\u001b[39m,\u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mCount\u001b[39m\u001b[38;5;124m\"\u001b[39m])\n\u001b[1;32m      4\u001b[0m \u001b[38;5;28mprint\u001b[39m(\u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mTime Set:\u001b[39m\u001b[38;5;124m\"\u001b[39m , sys\u001b[38;5;241m.\u001b[39margv)\n\u001b[0;32m----> 5\u001b[0m seconds_agrv \u001b[38;5;241m=\u001b[39m \u001b[38;5;28;43mfloat\u001b[39;49m\u001b[43m(\u001b[49m\u001b[43msys\u001b[49m\u001b[38;5;241;43m.\u001b[39;49m\u001b[43margv\u001b[49m\u001b[43m[\u001b[49m\u001b[38;5;241;43m1\u001b[39;49m\u001b[43m]\u001b[49m\u001b[43m)\u001b[49m\n\u001b[1;32m      6\u001b[0m \u001b[38;5;28;01mglobal\u001b[39;00m count\n\u001b[1;32m      7\u001b[0m count\u001b[38;5;241m=\u001b[39m\u001b[38;5;241m0\u001b[39m\n",
      "\u001b[0;31mValueError\u001b[0m: could not convert string to float: '-f'"
     ]
    }
   ],
   "source": [
    "file = open('RadData.csv','w',newline = None)\n",
    "csvwriter = csv.writer(file,delimiter=',')\n",
    "csvwriter.writerow([\"Real Time\",\"Seconds\",\"Count\"])\n",
    "print(\"Time Set:\" , sys.argv)\n",
    "seconds_agrv = float(sys.argv[1])\n",
    "global count\n",
    "count=0\n",
    "\n",
    "def my_callback():\n",
    "    print(\"Callback Ran\")\n",
    "    global count\n",
    "    count+=1\n",
    "i=0\n",
    "gp.add_event_detect(cnum, gp.FALLING,callback=my_callback)\n",
    "while i < seconds_agrv:\n",
    "    \n",
    "    Time = time.time()\n",
    "    if (i % 60 == 0):\n",
    "        csvwriter.writerow([i, count])\n",
    "        count=0\n",
    "    if i ==  seconds_argv:\n",
    "        csvwriter.writerow([Time, i, count])\n",
    "    i += 1\n",
    "    time.sleep(1)\n",
    "print(\"Ended loop\")\n",
    "file.close()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "d00d065f-4f21-48d6-8cab-61ad9d8ce8a1",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "1501f605-8b0c-4780-8c97-2813d9b6026e",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.9.2"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
