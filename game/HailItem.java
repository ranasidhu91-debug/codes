package game;

import edu.monash.fit2099.engine.Display;
import edu.monash.fit2099.engine.Item;
import edu.monash.fit2099.engine.Location;

import java.util.Random;

/***
 * A special class that when it's probability is less than 5%, it would summon the Voodoo Priestess Mambo Marie.
 * If Mambo Marie is alive after 30 turns, she would be removed from the game. She would re-appear at some point. If however
 * she dies before 30 turns, she would never be resurrected.
 */

public class HailItem extends Item {
    /**
     * Construtor for HailItem
     * @param name
     */
    public HailItem(String name){
        super(name,'I',false);
    }

    private MamboMarie marie = new MamboMarie();
    protected Random rand = new Random();
    private Display display = new Display();

    static int min = 0;
    static int max = 11;
    static boolean alive = true;
    private double percentage = 0.99;

    /**
     * Allows HailItem to feel the passage of time. If the probability is less than 5%, the map does not contain Mambo Marie
     * and that she has not been killed yet, HailItem would create a new Mambo Marie and add her into the map.
     * If she is still alive after 30 turns, she would be removed from the map and summoned again at some point in the future.
     * @param location the location of HailItem
     */
    @Override
    public void tick(Location location) {
        super.tick(location);
        if(rand.nextDouble()< percentage){
            if(!location.map().contains(marie)){
                if(alive){
                    min = 0;
                    location.map().at(0,17).addActor(marie);
                    display.println(marie.toString() + " has appeared");
                }

            }
        }
        if(location.map().contains(marie)){
            if(min == max){
                display.println(marie.toString() + " has disappeared");
                location.map().removeActor(marie);
            }
        }
    }

}