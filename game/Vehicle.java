package game;

import edu.monash.fit2099.engine.*;

/***
 * Special class that creates a vehicle to allow the player to move from one map to another.
 */
public class Vehicle extends Item {
    public Vehicle(){
        super("Jeep",'v',false);
    }

    public void addAction(Action action){
        this.allowableActions.add(action);
    }
}
