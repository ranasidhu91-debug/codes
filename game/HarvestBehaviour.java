package game;

import edu.monash.fit2099.engine.*;

import java.util.ArrayList;
import java.util.Collections;
import java.util.List;

public class HarvestBehaviour implements Behaviour {
    private ZombieCapability whatever;

    /**
     * Sets the team that the owner of this behaviour is allowed to harvest a ripe crop
     * @param whatever Team descriptor for ZombieActors that can harvest a ripe crop .
     */
    public HarvestBehaviour(ZombieCapability whatever){
        this.whatever = whatever;
    }

    /**
     * Returns a Harvest Action. It would take a list of all the places around the actor or the
     * location sthat the actor is standing on if such a location can be harvested as such a
     * ground would have the capability ZombieCapability.COMPLETE. Only actors with the ZombieCapability.FARM or
     * ZombieCapability.FOOD can harvest a ripe crop.
     * @param actor the Actor acting
     * @param map the GameMap containing the Actor
     * @return Harvest Action
     */
    @Override
    public Action getAction(Actor actor, GameMap map){
        List<Exit> exits = new ArrayList<Exit>(map.locationOf(actor).getExits());
        Collections.shuffle(exits);

        if(actor.hasCapability(ZombieCapability.FARM)||actor.hasCapability(ZombieCapability.FOOD)){
            for (Exit exit : exits){
                Ground ground = exit.getDestination().getGround();
                if (ground.hasCapability(ZombieCapability.COMPLETE)){
                    return new HarvestAction(exit.getDestination());
                }
            }
            if(map.locationOf(actor).getGround().hasCapability(ZombieCapability.COMPLETE)){
                return new HarvestAction(map.locationOf(actor));
            }
        }
        return null;
    }
}
