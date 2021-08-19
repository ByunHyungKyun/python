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



public class Main6 extends Application {
	@Override
	public void start(Stage primaryStage) {
		try {
			AnchorPane root = (AnchorPane)FXMLLoader.load(getClass().getResource("main6.fxml"));
			Scene scene = new Scene(root,400,400);
			scene.getStylesheets().add(getClass().getResource("application.css").toExternalForm());
			primaryStage.setScene(scene);
			primaryStage.show();
			//~(tf1)에서(label) ~(tf2) 까지짝수합(btn) (tf3)
			
			TextField txt = (TextField) scene.lookup("#tf1");
			TextField txt2 = (TextField) scene.lookup("#tf2");
			TextField txt3 = (TextField) scene.lookup("#tf3");

			Button btn = (Button) scene.lookup("#btn");
			btn.setOnMouseClicked(new EventHandler<Event>() {
				@Override
				public void handle(Event event) {
					int a1 = Integer.parseInt(txt.getText());
					int a2 = Integer.parseInt(txt2.getText());
					int a3 = 0;
					
					for(int i = a1;i<a2+1;i++) {
						if(i%2==0) {
							a3 += i;
						}
					}
					
					txt3.setText(Integer.toString(a3));
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
