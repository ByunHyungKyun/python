package application;
	
import javafx.application.Application;
import javafx.event.Event;
import javafx.event.EventHandler;
import javafx.fxml.FXMLLoader;
import javafx.stage.Stage;
import javafx.scene.Scene;
import javafx.scene.control.Button;
import javafx.scene.control.TextField;
import javafx.scene.layout.AnchorPane;



public class Main5 extends Application {
	@Override
	public void start(Stage primaryStage) {
		try {
			AnchorPane root = (AnchorPane)FXMLLoader.load(getClass().getResource("main5.fxml"));
			Scene scene = new Scene(root,400,400);
			scene.getStylesheets().add(getClass().getResource("application.css").toExternalForm());
			primaryStage.setScene(scene);
			primaryStage.show();
			
			
			TextField txt = (TextField) scene.lookup("#tfMine");
			TextField txt2 = (TextField) scene.lookup("#tfCom");
			TextField txt3 = (TextField) scene.lookup("#tfResult");

			Button btn = (Button) scene.lookup("#btn");
			btn.setOnMouseClicked(new EventHandler<Event>() {
				@Override
				public void handle(Event event) {
					
					double a = Math.random();
					
					if(a>0.5) {
						txt2.setText("Â¦");
					}else {
						txt2.setText("È¦");
					}
					
					if(txt2.getText().equals(txt.getText())) {
						txt3.setText("½Â¸®");
					}else {
						txt3.setText("ÆÐ¹è");
					}
					
					
				}
			});
		} catch(Exception e) {
			e.printStackTrace();
		}
	}
	
	public static void main(String[] args) {
		launch(args);
	}
}
