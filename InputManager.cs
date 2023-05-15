using System.Collection;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.InputSystem;


public class InputManager: MonoBehaviour
{
    private PlayerInput playerInput;
    private PlayerInput.OnFootActions onFoot;


    // void start method not needed
    void Awake()
    {
        // player input instance
        playerInput = new PlayerInput();
        onFoot = playerInput.OnFoot;
        // instance of the player motor component
        motor = GetComponent<PlayerMotor>();


    }

    // update is called once per frame
    void FixedUpdate()
    {
        // tell the player motor to move using the value from our movement action
        motor.ProcessMove(onFoot.Movement.ReadValue<vector2>());



    }

    private void onEnable()
    {
        onFoot.Enable();
    }

    private void onDisable()
    {
        onFoot.Disable();
    }
}