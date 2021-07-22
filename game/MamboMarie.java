package game;

import edu.monash.fit2099.engine.*;

/**
 * A class that creates the Voodoo Priestess named Mambo Marie that is responsible for the Zombie outbreak in the game.
 */
public class MamboMarie extends ZombieActor{
    private Display display = new Display();

    private int min = 0;

    private Behaviour wander = new WanderBehaviour();

    /***
     * A constructor that creates Mambo Marie
     */
    public MamboMarie(){
        super("Mambo Marie",'M',100,ZombieCapability.UNDEAD);
        addCapability(ZombieCapability.ARISE);
    }

    /***
     * In 9 turns, Mambo Marie wanders the map. However, in it's 10th turn, it would summon 5 new Zombies to infest the game.
     * @param actions    collection of possible Actions for this Actor
     * @param lastAction The Action this Actor took last turn. Can do interesting things in conjunction with Action.getNextAction()
     * @param map        the map containing the Actor
     * @param display    the I/O object to which messages may be written
     * @return the action that Mambo Marie did.
     */
    @Override
    public Action playTurn(Actions actions, Action lastAction, GameMap map, Display display){
        min ++;
        HailItem.min ++;
        if(min == 5){
            display.println(this.toString() + " chants 'ARISE AND KILL THE DOOMSLAYER");
            Action calls = new SummonAction(map);
            min = 0;
            return calls;
        }
        if(min < 10){
            return wander.getAction(this,map);
        }

        return new DoNothingAction();

    }
}