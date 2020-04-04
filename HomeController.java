package com.spring.controller;

import java.io.BufferedReader;
import java.io.File;
import java.io.FileReader;
import java.io.FileWriter;
import java.text.DateFormat;
import java.util.Date;
import java.util.Locale;

import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestMethod;
import org.springframework.web.bind.annotation.ResponseBody;

import lombok.extern.slf4j.Slf4j;

@Controller
@Slf4j
public class HomeController {
	
	@RequestMapping(value = "/", method = RequestMethod.GET)
	public String home() {
//		log.info("index 페이지 요청");
		
		return "index";
	}
	@GetMapping("/umbrella")
	public String umbrella() {
//		log.info("umbrella 페이지 요청");
		
		return "umbrella2";
	}
	
	@PostMapping("/umbrella/save_center")
	public void umbrella_save_center(String center_lat, String center_lng, String user_uuid) {
		
		File file = new File("e:\\"+user_uuid+"center.txt");
		FileWriter writer = null;
		
		try {
			writer = new FileWriter(file, false);
			writer.write(center_lat+" "+center_lng);
			writer.flush();
			
			
		} catch (Exception e) {
			e.printStackTrace();
		}finally {
			try {
				if(writer != null) {
					writer.close();
				}
			} catch (Exception e2) {
				e2.printStackTrace();
			}
		}
		System.out.println("saveCenter_done");
	}
	
	@PostMapping("/umbrella/get_center")
	@ResponseBody
	public String umbrella_get_center(String user_uuid) {
		String latlng = "";
		File file = new File("e:\\"+user_uuid+"center.txt");
		try(FileReader filereader = new FileReader(file);
			BufferedReader br = new BufferedReader(filereader)
			) {
			latlng = br.readLine();
			
			
		} catch (Exception e) {
			e.printStackTrace();
		}
		

		System.out.println("getCenter_done"+latlng);
		return latlng;
	}

	
	@PostMapping("/umbrella/save_level")
	public void umbrella_save_level(String level, String user_uuid) {
		
		File file = new File("e:\\"+user_uuid+"level.txt");
		FileWriter writer = null;
		
		try {
			writer = new FileWriter(file, false);
			writer.write(level);
			writer.flush();
			
			System.out.println("done");
		} catch (Exception e) {
			e.printStackTrace();
		}finally {
			try {
				if(writer != null) {
					writer.close();
				}
			} catch (Exception e2) {
				e2.printStackTrace();
			}
		}
		
	}
	
	@PostMapping("/umbrella/get_level")
	@ResponseBody
	public String umbrella_get_level(String user_uuid) {
		String level = "";
		File file = new File("e:\\"+user_uuid+"level.txt");
		try(FileReader filereader = new FileReader(file);
			BufferedReader br = new BufferedReader(filereader)
			) {
			level = br.readLine();
			System.out.println("get_level1 : "+level);
			
		} catch (Exception e) {
			e.printStackTrace();
		}
		System.out.println("get_level2 : "+level);
		return level;
	}
	@GetMapping("/umbrella/mkimg")
	public String mkimg() {
		return "mkimg";
	}
}
