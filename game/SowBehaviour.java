package game;

import edu.monash.fit2099.engine.*;

import java.util.ArrayList;
import java.util.Collections;
import java.util.List;
import java.util.Random;

/**
 * A class that generates either a Sowing action or fertilize action.
 */

public class SowBehaviour implements Behaviour{
    private ZombieCapability whatever;
    protected Random rand = new Random();

    /**
     * Sets the team that the owner of this behaviour is allowed to sow crop onto dirt.
     * @param whatever Team descriptor for ZombieActors that can sow crop on dirt.
     */

    public SowBehaviour(ZombieCapability whatever){
        this.whatever = whatever;
    }

    /**
     * Returns a SowAction or FertilizeAction that either sows a crop on dirt or fertilizes a crop.
     * Dirt can only be sowed with crops if the farmer has "whatever" capability.
     * @param actor the Actor acting
     * @param map the GameMap containing the Actor
     * @return SowAction or FertilizeAction
     */
    @Override
    public Action getAction(Actor actor,GameMap map){
        List<Exit> exits = new ArrayList<Exit>(map.locationOf(actor).getExits());
        Collections.shuffle(exits);

        if(actor.hasCapability(whatever)){
            for (Exit e:exits){
                char dirtSpace = e.getDestination().getGround().getDisplayChar();
                if(dirtSpace == '.'){
                    if(rand.nextDouble()<0.34){
                        return new SowAction(e.getDestination());
                    }
                }
            }
            if(map.locationOf(actor).getGround() instanceof Crop){
                return new FertilizeAction(map.locationOf(actor).getGround());
            }
        }
        return null;
    }
}
