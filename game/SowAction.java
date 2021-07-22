package game;

import edu.monash.fit2099.engine.*;

/**
 * Special class for sowing crop onto a patch of dirt.
 */
public class SowAction extends Action {

    /**
     * The location where the crop would be sowed.
     */
    protected Location target;

    /**
     * Constructor
     * @param target location where the crop would be sowed.
     */
    public SowAction(Location target){
        this.target = target;
    }

    /**
     * Performs the action of creating a new crop. The actor would be able to sow the crop onto the patch of dirt.
     * @param actor The actor performing the action.
     * @param map The map the actor is on.
     * @return A description of what happened that would be displayed to the user.
     */
    @Override
    public String execute(Actor actor,GameMap map){
        Crop crop = new Crop();

        target.setGround(crop);

        return actor + " sowed crop on dirt";
    }

    /**
     * Returns a descriptive String
     * @param actor The actor performing the action.
     * @return the text we put on the menu.
     */
    @Override
    public String menuDescription(Actor actor){
        return actor + " sows ground";
    }

}
