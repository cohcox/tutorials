using System;
using UnityEngine;

public class Clock : MonoBehaviour
{
    const float hoursToDegrees = -30f, minsToDegrees = -6f, secToDegrees = -6f;

    [SerializeField]
    Transform hrsPivot, minsPivot, secPivot;

    private void Update()
    {
        TimeSpan time = DateTime.Now.TimeOfDay;
        hrsPivot.localRotation = Quaternion.Euler(0f, 0f, hoursToDegrees * (float)time.TotalHours);
        minsPivot.localRotation = Quaternion.Euler(0f, 0f, minsToDegrees * (float)time.TotalMinutes);
        secPivot.localRotation = Quaternion.Euler(0f, 0f, secToDegrees * (float)time.TotalSeconds);
    }
}
