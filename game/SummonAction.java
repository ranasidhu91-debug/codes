package game;

import edu.monash.fit2099.engine.*;

import java.util.ArrayList;
import java.util.List;
import java.util.Random;

public class SummonAction extends Action {

    private String letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";
    protected GameMap target;

    public SummonAction(GameMap target){
        this.target = target;
    }


    public String nameGenerator(String name){
        Random random = new Random();
        StringBuilder names = new StringBuilder();
        for (int i = 0;i < 5;i++){
            int index = random.nextInt(name.length());
            names.append(name.charAt(index));
        }
        return names.toString();
    }

    @Override
    public String execute(Actor actor,GameMap map){

        List<String> names = new ArrayList<>();
        for(int i = 0;i < 5;i++){
            String name = nameGenerator(letters);
            names.add(name);
        }
        int a,b;
        for(String name:names){
            do {
                a = (int) Math.floor(Math.random() * 10 + 40.0);
                b = (int) Math.floor(Math.random() * 2 + 20.0);
            }
            while (map.at(a,b).containsAnActor());
            map.at(a,b).addActor(new Zombie(name));
        }
        return actor + " spawned 5 zombies";
    }

    @Override
    public String menuDescription(Actor actor){
        return actor + " summons 5 zombies.";
    }

}