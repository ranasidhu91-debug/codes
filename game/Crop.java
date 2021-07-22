package game;

import edu.monash.fit2099.engine.*;

/**
 *  A class to create crop
 */
public class Crop extends Ground {
    private int turns = 0;

    /**
     * Constructor for crop.
     */
    public Crop(){
        super('c');
    }

    /**
     * Crop feels the passage of time. The crop would ripe in 20 turns but if a farmer fertilizes it, it would increase
     * the speed of ripening by 10 turns.
     * @param location The location of the Ground
     */
    @Override
    public void tick(Location location){
        super.tick(location);

        Actor actor = location.getActor();
        if(hasCapability(ZombieCapability.FERTILIZE)){
            if(actor instanceof Farmer){
                turns += 10;
            }
            else{
                turns ++;
            }
        }
        else{
            turns ++;
        }

        if (turns > 20 || turns == 20){
            displayChar = 'R';
            addCapability(ZombieCapability.COMPLETE);
        }
    }
}
