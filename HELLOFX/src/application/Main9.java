package application;
	
import javafx.application.Application;
import javafx.event.Event;
import javafx.event.EventHandler;
import javafx.fxml.FXMLLoader;
import javafx.stage.Stage;
import javafx.scene.Scene;
import javafx.scene.control.Alert;
import javafx.scene.control.Alert.AlertType;
import javafx.scene.control.Button;
import javafx.scene.control.TextField;
import javafx.scene.layout.AnchorPane;


public class Main9 extends Application {
	TextField tf;
	@Override
	public void start(Stage primaryStage) {
		try {
			AnchorPane root = (AnchorPane)FXMLLoader.load(getClass().getResource("main9.fxml"));
			Scene scene = new Scene(root,400,400);
			scene.getStylesheets().add(getClass().getResource("application.css").toExternalForm());
			primaryStage.setScene(scene);
			primaryStage.show();
			//(tf)
			//1(btn1) 2(btn2) 3(btn3)
			//4(btn4) 5(btn5) 6(btn6)
			//7(btn7) 8(btn8) 9(btn9)
			// call(btnCall)
			

			tf = (TextField) scene.lookup("#tf");
			
			Button btn = (Button) scene.lookup("#btn1");
			btn.setOnMouseClicked(new EventHandler<Event>() {
				@Override
				public void handle(Event event) {
					myClick("1");
				}
			});
			
			Button btn2 = (Button) scene.lookup("#btn2");
			btn2.setOnMouseClicked(new EventHandler<Event>() {
				@Override
				public void handle(Event event) {
					myClick("2");
				}
			});
			
			Button btn3 = (Button) scene.lookup("#btn3");
			btn3.setOnMouseClicked(new EventHandler<Event>() {
				@Override
				public void handle(Event event) {
					myClick("3");
				}
			});
			
			Button btn4 = (Button) scene.lookup("#btn4");
			btn4.setOnMouseClicked(new EventHandler<Event>() {
				@Override
				public void handle(Event event) {
					myClick("4");
				}
			});
			
			Button btn5 = (Button) scene.lookup("#btn5");
			btn5.setOnMouseClicked(new EventHandler<Event>() {
				@Override
				public void handle(Event event) {
					myClick("5");
				}
			});
			
			Button btn6 = (Button) scene.lookup("#btn6");
			btn6.setOnMouseClicked(new EventHandler<Event>() {
				@Override
				public void handle(Event event) {
					myClick("6");
				}
			});
			
			Button btn7 = (Button) scene.lookup("#btn7");
			btn7.setOnMouseClicked(new EventHandler<Event>() {
				@Override
				public void handle(Event event) {
					myClick("7");
				}
			});
			
			Button btn8 = (Button) scene.lookup("#btn8");
			btn8.setOnMouseClicked(new EventHandler<Event>() {
				@Override
				public void handle(Event event) {
					myClick("8");
				}
			});
			
			Button btn9 = (Button) scene.lookup("#btn9");
			btn9.setOnMouseClicked(new EventHandler<Event>() {
				@Override
				public void handle(Event event) {
					myClick("9");
				}
			});
			
			Button btn0 = (Button) scene.lookup("#btn0");
			btn0.setOnMouseClicked(new EventHandler<Event>() {
				@Override
				public void handle(Event event) {
					myClick("0");
				}
			});
			
			Button btn12 = (Button) scene.lookup("#btn-");
			btn12.setOnMouseClicked(new EventHandler<Event>() {
				@Override
				public void handle(Event event) {
					myClick("-");
				}
			});
			
			Button btnCall = (Button) scene.lookup("#btnCall");
			btnCall.setOnMouseClicked(new EventHandler<Event>() {
				@Override
				public void handle(Event event) {
					Alert alert = new Alert(AlertType.INFORMATION);
					alert.setTitle("Call");
					alert.setHeaderText("Calling~~");
					alert.setContentText(tf.getText());

					alert.showAndWait();

				}
			});
			
			
		} catch(Exception e) {
			e.printStackTrace();
		}
	}
	
	
	
	
	public void myClick(String str_new) {
		
		String str_old = tf.getText();
		
		tf.setText(str_old+str_new);
		
	}
	
	
	
	public static void main(String[] args) {
		launch(args);
	}
}
