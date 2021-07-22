package game;

/**
 * A class to create Food.
 */
public class Food extends PortableItem {
    /**
     * Constructor class for food that a human can eat to restore health. Has capabilities ZombieCapability.FOOD and
     * ZombieCapability.FARM.
     * @param name Name of food
     * @param displayChar Character displayed on map.
     */
    public Food(String name,char displayChar){
        super(name,displayChar);

        addCapability(ZombieCapability.FOOD);
        addCapability(ZombieCapability.FARM);
    }


}
