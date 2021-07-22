package game;

import edu.monash.fit2099.engine.*;


import java.util.Arrays;
import java.util.Collections;


/**
 * Class representing Farmer which is a type of Human.
 */
public class Farmer extends Human {
    /**
     * A list of behaviours that are possible by the farmer.
     */
    public Behaviour[] behaviours = {
            new SowBehaviour(ZombieCapability.FARM),
            new WanderBehaviour(),
            new HarvestBehaviour(ZombieCapability.FARM),
            new EatBehaviour(ZombieCapability.FARM),
            new PickDropBehaviour(ZombieCapability.FARM)
    };

    /**
     * A constructor class for Farmer. All farmer's are instantiated with the capability to FARM.
     * @param name Name of the Farmer
     */
    public Farmer(String name){
        super(name,'F',100);

        addCapability(ZombieCapability.FARM);
    }

    /**
     * At each turn, the farmer would be either able to sow crop on dirt, fertilize it, wander the map, harvest ripe crop
     * for food which would enable all types of humans to eat it and pick up or drop off portable items.
     * @param actions list of possible actions
     * @param lastAction the previous action if it was a multi-turn action.
     * @param map the map the farmer is on.
     * @param display the display where the Farmer utterances are shown.
     * @return the action that the farmer did.
     */
    @Override
    public Action playTurn(Actions actions, Action lastAction, GameMap map, Display display){
        Collections.shuffle(Arrays.asList(behaviours));
        for (Behaviour behaviour : behaviours){
            Action action = behaviour.getAction(this,map);
            if(action != null){
                return action;
            }
        }
        return new DoNothingAction();
    }
}
