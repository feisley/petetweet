// ActionScript file
package com.petetweet.client.events
{
	import flash.events.Event;

	public class ReplyEvent extends Event
	{
		public function ReplyEvent(username:String, bubbles:Boolean=true, cancelable:Boolean=false)
		{
			super("ReplyEvent", bubbles, cancelable);
			
			this.username = username;
		}
		
		public var username:String;
		
		override public function clone():Event {
			return new ReplyEvent(username);
		}
		
	}
}