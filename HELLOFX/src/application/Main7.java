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



public class Main7 extends Application {
	@Override
	public void start(Stage primaryStage) {
		try {
			AnchorPane root = (AnchorPane)FXMLLoader.load(getClass().getResource("main7.fxml"));
			Scene scene = new Scene(root,400,400);
			scene.getStylesheets().add(getClass().getResource("application.css").toExternalForm());
			primaryStage.setScene(scene);
			primaryStage.show();
			//나 : 가위바위보 (tfMine)
			//컴 : (tfCom)
			//결과 : (tfResult)
			//결과보기(btn)
			
			TextField txt = (TextField) scene.lookup("#tfMine");
			TextField txt2 = (TextField) scene.lookup("#tfCom");
			TextField txt3 = (TextField) scene.lookup("#tfResult");

			Button btn = (Button) scene.lookup("#btn");
			btn.setOnMouseClicked(new EventHandler<Event>() {
				@Override
				public void handle(Event event) {
					
					double a = Math.random();
					
					if(a>0.33) {
						txt2.setText("가위");
					}else if(0.66>a && 0.33<a){
						txt2.setText("바위");
					}else {
						txt2.setText("보");
					}
					
					if(txt2.getText().equals("가위")) {
						if(txt.getText().equals("바위")) {
							txt3.setText("승리");
						}else if (txt.getText().equals("보")) {
							txt3.setText("패배");
						}else {
							txt3.setText("비김");
						}
					}else if(txt2.getText().equals("바위")) {
						if(txt.getText().equals("보")) {
							txt3.setText("승리");
						}else if (txt.getText().equals("가위")) {
							txt3.setText("패배");
						}else {
							txt3.setText("비김");
						}
					}else {
						if(txt.getText().equals("가위")) {
							txt3.setText("승리");
						}else if (txt.getText().equals("바위")) {
							txt3.setText("패배");
						}else {
							txt3.setText("비김");
						}
						
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
